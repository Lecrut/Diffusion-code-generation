def combine_lists(large_list_a, large_list_b):
    it_a = iter(large_list_a)
    it_b = iter(large_list_b)
    while True:
        try:
            item_a = next(it_a)
            yield item_a
        except StopIteration:
            break
    for item in it_b:
        yield item

if __name__ == '__main__':
    large_list_a = list(range(1000000))
    large_list_b = list(range(1000000, 2000000))
    combined_generator = combine_lists(large_list_a, large_list_b)
    result_list = []
    for _ in range(10):
        result_list.append(next(combined_generator))
    print(result_list)