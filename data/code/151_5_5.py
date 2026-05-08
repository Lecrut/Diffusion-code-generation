def combine_lists(large_list_a, large_list_b):
    for item in large_list_a:
        yield item
    for item in large_list_b:
        yield item
if __name__ == '__main__':
    list_a = list(range(1000000))
    list_b = list(range(1000000, 2000000))
    combined_generator = combine_lists(list_a, list_b)
    print("First 10 elements:")
    for i in range(10):
        print(next(combined_generator))
    print("\nNext 10 elements:")
    for i in range(10):
        print(next(combined_generator))
    print("\nLast 10 elements:")
    for i in range(10):
        print(next(combined_generator))