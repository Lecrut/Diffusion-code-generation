def reverse_and_sort_names(names):
    if not all(isinstance(name, str) for name in names):
        raise ValueError("All elements in the list must be strings.")
    
    reversed_names = [name[::-1] for name in names]
    reversed_names.sort()
    return reversed_names

if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Original List:", sample_list)
    result = reverse_and_sort_names(sample_list)
    print("Reversed and Sorted Names:", result)