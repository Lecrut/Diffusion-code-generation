def combine_lists(large_list_a, large_list_b):
    it_a = iter(large_list_a)
    it_b = iter(large_list_b)
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
    print("First 10 elements:")
    for i in range(10):
        print(next(combined_generator))
    print("\nNext 10 elements:")
    for i in range(10):
        print(next(combined_generator))