def determine_cluster_key(fruit_type):
    citrus_keywords = ['orange', 'lemon', 'lime']
    berry_keywords = ['strawberry', 'blueberry', 'raspberry']
    if fruit_type.lower() in [k for k in citrus_keywords]:
        return "Citrus"
    if fruit_type.lower() in [k for k in berry_keywords]:
        return "Berry"
    return f"Other_{fruit_type[0].upper()}"
def sort_fruits_by_cluster(fruit_list):
    return [(determine_cluster_key(f), f) for f in fruit_list]
def cluster_fruits_advanced(fruit_types):
    if not fruit_types:
        return []
    sorted_items = [(determine_cluster_key(f), f) for f in fruit_types]
    sorted_items.sort(key=lambda x: x[0])
    clusters = []
    current_group_members = []
    last_key = None
    for key, fruit in sorted_items:
        if key != last_key and current_group_members:
            clusters.append({
                "type": key,
                "members": [m[1] for m in current_group_members],                                      
                "_count": len(current_group_members)
            })
            current_group_members = []
        last_key = key
        current_group_members.append((key, fruit))
    if current_group_members:
        clusters.append({
            "type": last_key,
            "members": [m[1] for m in current_group_members],
            "_count": len(current_group_members)
        })
    return clusters
if __name__ == '__main__':
    raw_fruit_data = ["Apple", "Banana", "Orange", "Lemon", 
                      "Strawberry", "Blueberry", "Raspberry"]
    print("Clustering Fruits by Type Pattern...")
    result_clusters = cluster_fruits_advanced(raw_fruit_data)
    for i, cluster in enumerate(result_clusters):
        print(f"\nCluster {i+1}: '{cluster['type']}'")
        if "_count" in cluster:
            print(f"  Count: {cluster['_count']} members")
        sorted_members = sorted(cluster["members"])
        for member in sorted_members:
            print(f"    - {member}")
    print("\nClustering complete.")