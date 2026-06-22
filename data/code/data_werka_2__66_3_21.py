def adjacent_pairs_generator(lst):
    for i in range(len(lst) - 1):
        is_less_than = lst[i] < lst[i + 1]
        yield is_less_than

if __name__ == '__main__':
    sample_list_1 = [5, 2, 8, 6, 9]
    sample_list_2 = [10, 10, 10]
    sample_list_3 = [1, 2, 3, 4, 5]

    print("Sample List 1 Results:")
    for result in adjacent_pairs_generator(sample_list_1):
        print(result)

    print("\nSample List 2 Results:")
    for result in adjacent_pairs_generator(sample_list_2):
        print(result)

    print("\nSample List 3 Results:")
    for result in adjacent_pairs_generator(sample_list_3):
        print(result)