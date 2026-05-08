def combine_lists(list_a, list_b):
    it_a = iter(list_a)
    it_b = iter(list_b)
    while True:
        try:
            item_a = next(it_a)
            yield item_a
        except StopIteration:
            try:
                item_b = next(it_b)
                yield item_b
            except StopIteration:
                break
if __name__ == '__main__':
    large_list_a = list(range(1000000))
    large_list_b = list(range(1000000, 2000000))
    combined_generator = combine_lists(large_list_a, large_list_b)
    result_list = []
    for item in combined_generator:
        result_list.append(item)
    print(f"First 10 elements of the combined sequence:")
    for i in range(10):
        try:
            print(combined_generator.__next__())
        except StopIteration:
            break
    print(f"\nTotal elements collected: {len(result_list)}")