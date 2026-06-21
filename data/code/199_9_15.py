def reverse_and_sort_names(names):
    reversed_names = [name[::-1] for name in names]
    reversed_names.sort()
    return reversed_names

if __name__ == '__main__':
    sample_list = ["Charlie", "Alice", "Bob", "David"]
    print("Original List:", sample_list)
    result = reverse_and_sort_names(sample_list)
    print("\nReversed and Sorted Names:")
    for name in result:
        print(name)