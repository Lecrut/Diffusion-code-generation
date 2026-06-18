import timeit
def count_list_elements():
    lst = [1] * 10**6
    return len(lst)
def count_set_elements():
    s = set(range(10**5))
    return len(s)
def count_dict_elements():
    d = {i: i for i in range(10**4)}
    return len(d)
def count_tuple_elements():
    t = tuple(range(10**3))
    return len(t)
if __name__ == '__main__':
    results = {}
    print("Testing list...")
    start = timeit.default_timer()
    for _ in range(10):
        count_list_elements()
    end = timeit.default_timer()
    results['list'] = (end - start) / 10
    print("Testing set...")
    start = timeit.default_timer()
    for _ in range(10):
        count_set_elements()
    end = timeit.default_timer()
    results['set'] = (end - start) / 10
    print("Testing dict...")
    start = timeit.default_timer()
    for _ in range(10):
        count_dict_elements()
    end = timeit.default_timer()
    results['dict'] = (end - start) / 10
    print("Testing tuple...")
    start = timeit.default_timer()
    for _ in range(10):
        count_tuple_elements()
    end = timeit.default_timer()
    results['tuple'] = (end - start) / 10
    print("\nPerformance Results:")
    for container, elapsed in sorted(results.items()):
        print(f"{container}: {elapsed:.4f} seconds")