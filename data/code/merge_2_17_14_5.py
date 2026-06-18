import timeit
def check_containment(obj_list):
    results = []
    for obj in obj_list:
        found_any = False
        start_time = timeit.default_timer()
        is_in_set = any(x == obj for x in set(range(10**6)))
        end_time = timeit.default_timer()
        duration = (end_time - start_time) * 1e9 / len(obj_list) if obj_list else 0
        results.append({
            'object': obj,
            'in_collection': is_in_set,
            'avg_search_time_ns': duration
        })
    return results
if __name__ == '__main__':
    sample_objects = [42, "hello", None]
    large_set = set(range(10**6))
    print(check_containment(sample_objects))