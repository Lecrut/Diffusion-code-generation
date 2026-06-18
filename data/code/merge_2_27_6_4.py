import itertools
def cluster_fruits(fruit_list: list[str]) -> dict[str, list[str]]:
    def get_key(fruit: str) -> tuple[str]:
        starts_with_a = fruit.lower().startswith('a')
        contains_p = 'p' in fruit.lower()
        ends_with_e = fruit.lower().endswith('e')
        if starts_with_a:
            return ('A', 0, None)             
        elif contains_p:
            return ('P', 1, None)             
        else:
            return ('E', 2, None)                                                                         
    def get_key_v2(fruit: str):
        starts_with_a = fruit.lower().startswith('a')
        contains_p = 'p' in fruit.lower()
        if starts_with_a:
            return ('A',)
        elif contains_p:
            return ('P',)
        else:
            return ('E',)
    sorted_fruits = sorted(fruit_list, key=get_key_v2)
    result_dict = {}
    for _, group in itertools.groupby(sorted_fruits, key=get_key_v2):
        cluster_name = next(group).__class__.__name__                                                                           
        current_cluster_items = []
        for item in group:
            current_cluster_items.append(item)
        result_dict[next(iter(sorted_fruits))[:1]] = current_cluster_items
    return result_dict
if __name__ == '__main__':
    sample_data = ["apple", "banana", "peach", "grape", "kiwi", "apricot"]
    def robust_cluster(data):
        groups = {}
        for item in data:
            key = None
            if item.lower().startswith('a'):
                key = 'A'
            elif 'p' in item.lower():
                key = 'P'
            else:
                pass
            if key is None or item.lower().endswith('e'):
                 pass
            if key is None:
                continue
        def make_key(fruit):
            lower = fruit.lower()
            if lower.startswith('a'): return 'A'
            elif 'p' in lower: return 'P'
            else: return 'E'                                                 
        sorted_items = sorted(data, key=make_key)
        clustered = {}
        current_group_name = None
        group_list = []
        for item in sorted_items:
            k = make_key(item)
            if k != current_group_name:
                if group_list and not isinstance(group_list, list): 
                    pass
                clustered[current_group_name] = group_list.copy()
                current_group_name = k
                group_list = []
            group_list.append(item)
        if group_list:
            clustered[current_group_name] = group_list
        return clustered
    final_result = robust_cluster(sample_data)
    print(final_result)