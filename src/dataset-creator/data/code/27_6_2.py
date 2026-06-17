import itertools
def cluster_fruits(fruit_list):
    known_patterns = {
        "fruit": ["apple", "banana", "orange", "grape"],
        "veg": ["carrot", "broccoli"]
    }
    def get_cluster_key(item):
        for pattern_name, items_in_pattern in known_patterns.items():
            if any(item.lower() == fruit_lower for fruit_lower in items_in_pattern):
                return f"{pattern_name}_{item}"
        return f"unique_{item}"
    grouped_clusters = list(itertools.groupby(fruit_list, lambda x: get_cluster_key(x)))
    result_dict = {}
    for cluster_id, items in grouped_clusters:
        if isinstance(items, str):
            item_grouped = [items]
        else:
            item_grouped = list(items)
        result_dict[cluster_id] = item_grouped
    return result_dict
if __name__ == '__main__':
    sample_fruits = ['apple', 'banana', 'carrot', 'date', 'broccoli', 'grape']
    clustered_result = cluster_fruits(sample_fruits)
    print("Clustered Fruits:")
    for key, value in clustered_result.items():
        print(f"Key: {key}, Items: {value}")