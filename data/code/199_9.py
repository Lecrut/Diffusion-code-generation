def shuffle_names(names):
    import random
    random.shuffle(names)
def sort_names(names):
    names.sort()
def remove_duplicates(names):
    seen = set()
    result = []
    for name in names:
        if name not in seen:
            seen.add(name)
            result.append(name)
    names[:] = result
if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]
    print("Original List:", sample_list)
    print("\n--- Testing Shuffle ---")
    shuffle_names(sample_list)
    print("Shuffled List:", sample_list)
    sample_list_2 = ["Zoe", "Adam", "Ben", "Zoe", "Charlie"]
    print("\nOriginal List 2:", sample_list_2)
    shuffle_names(sample_list_2)
    print("Shuffled List 2:", sample_list_2)
    print("\n--- Testing Sort ---")
    sort_names(sample_list)
    print("Sorted List:", sample_list)
    sample_list_3 = ["Charlie", "Alice", "Bob", "Alice", "David", "Charlie"]
    print("\nOriginal List 3:", sample_list_3)
    sort_names(sample_list_3)
    print("Sorted List 3:", sample_list_3)
    print("\n--- Testing Remove Duplicates ---")
    remove_duplicates(sample_list)
    print("List after removing duplicates (from first test):", sample_list)
    sample_list_4 = ["Apple", "Banana", "Apple", "Cherry", "Banana"]
    print("\nOriginal List 4:", sample_list_4)
    remove_duplicates(sample_list_4)
    print("List after removing duplicates (from second test):", sample_list_4)