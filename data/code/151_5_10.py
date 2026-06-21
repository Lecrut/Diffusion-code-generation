def combine_lists(large_list_a, large_list_b):
    it_a = iter(large_list_a)
    it_b = iter(large_list_b)
    result = []
    while True:
        try:
            item_a = next(it_a)
            result.append(item_a)
        except StopIteration:
            break
    while True:
        try:
            item_b = next(it_b)
            result.append(item_b)
        except StopIteration:
            break
    return result

if __name__ == '__main__':
    large_list_a = list(range(1000000))
    large_list_b = list(range(1000000, 2000000))
    combined_list = combine_lists(large_list_a, large_list_b)
    print("First 10 elements:", combined_list[:10])