import itertools
from typing import List, Tuple
def cluster_fruits(
    fruits: List[str], 
    category_keywords: dict
) -> List[Tuple[List[str], str]]:
    normalized_keywords = {k.lower(): [w.lower() for w in v] for k, v in category_keywords.items()}
    item_clusters = {}
    def is_match(fruit_lower: str, keywords_list: List[str]) -> bool:
        return any(kw in fruit_lower for kw in keywords_list)
    for cat_name, cats_kws in normalized_keywords.items():
        for f in fruits:
            if not item_clusters.get(f.lower()):
                if is_match(f.lower(), cats_kws):
                    item_clusters[f.lower()] = cat_name
    grouped_items = [(cat_name, f) for f in fruits 
                     for cat_name in [item_clusters.get(f.lower()) or "unknown"]]
    sorted_with_index = list(enumerate(grouped_items))
    sorted_by_cat_idx = sorted(sorted_with_index, key=lambda x: (x[1][0], x[0]))
    ordered_pairs = [item[1] for item in sorted_by_cat_idx]
    result_clusters = []
    if not ordered_pairs:
        return result_clusters
    current_cluster_items = [ordered_pairs[0][1]] 
    current_category_key = ordered_pairs[0][0] 
    for i in range(1, len(ordered_pairs)):
        item_fruit_cat = ordered_pairs[i]
        if item_fruit_cat == current_cluster_items[-1]:
            continue                                                                  
        elif item_fruit_cat[0] == current_category_key:
            current_cluster_items.append(ordered_pairs[i][1])
        else:
            result_clusters.append((current_cluster_items, current_category_key))
            current_cluster_items = [item_fruit_cat[1]] 
            current_category_key = item_fruit_cat[0]
    if current_cluster_items:
        result_clusters.append((current_cluster_items, current_category_key))
    return result_clusters
if __name__ == '__main__':
    sample_fruits = ["Apple", "Banana", "Orange", "Strawberry", "Lemon", "Grape"]
    category_patterns = {
        "citrus": ["orange", "lemon"], 
        "berries": ["strawberry"], 
        "stone": ["grape"],
        "general": []                                                                                                                              
    }
    clusters = cluster_fruits(sample_fruits, category_patterns)
    print("Fruit Clustering Results:")
    for group, cat_name in clusters:
        print(f"Category '{cat_name}': {', '.join(group)}")