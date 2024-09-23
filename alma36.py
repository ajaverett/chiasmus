import pandas as pd
pd.set_option('future.no_silent_downcasting', True)

df = pd\
    .read_excel('alma36.xlsx')\
    .query("c == 36")\
    .drop(columns=['c', 'v', 'scripture_text'])\
    .replace("x", 1)\
    .fillna(0)\
    .sum()\
    .reset_index()\
    .rename(columns={'index': 'element', 0: 'count'})\
    .assign(count = lambda x: x['count'].astype(int))

num_elements_chiastic = df\
    .query("element.str.match('^[A-Z]$')")\
    .shape[0]

num_appearances_chiastic = df\
    .query("element.str.match('^[A-Z]$')")\
    ['count'].astype(str).str.cat(sep=',')

num_elements_non_chiastic = df\
    .query("~element.str.match('^[A-Z]$')")\
    .shape[0]

num_appearances_non_chiastic = df\
    .query("~element.str.match('^[A-Z]$')")\
    ['count'].astype(str).str.cat(sep=',')

print(f"Chiastic elements: {num_elements_chiastic} ({num_appearances_chiastic})")
print(f"Non-chiastic elements: {num_elements_non_chiastic} ({num_appearances_non_chiastic})")
