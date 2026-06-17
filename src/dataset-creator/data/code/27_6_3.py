import itertools
def cluster_fruits(fruit_list):
    keywords = ('citrus', 'berry')
    clusters = {kw: [] for kw in keywords}
    other_cluster = None
    for fruit in fruit_list:
        matched_keyword = False
        for keyword in keywords:
            if keyword.lower() in fruit.lower():
                clusters[keyword].append(fruit)
                matched_keyword = True
                break                                                      
        if not matched_keyword and other_cluster is None:
            other_cluster = []
        if other_cluster is not None:
            other_cluster.append(fruit)
    return clusters
if __name__ == '__main__':
    sample_fruits = ['apple', 'orange', 'grapefruit', 'banana', 'strawberry', 
                     'mango', 'blueberry', 'pineapple']
    result_clusters = cluster_fruits(sample_fruits)
    for category, items in sorted(result_clusters.items()):
        print(f"{category.capitalize()}: {items}")