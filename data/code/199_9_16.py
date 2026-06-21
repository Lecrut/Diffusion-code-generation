def reverse_and_sort_names(names):
    reversed_sorted_names = sorted(name[::-1] for name in names)
    return reversed_sorted_names

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie"]
    result = reverse_and_sort_names(sample_names)
    print(result)