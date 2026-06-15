def shuffle_names(names):
    import random
    random.shuffle(names)
def sort_names(names):
    names.sort()
def remove_duplicates(names):
    unique_names = set(names)
    names[:] = list(unique_names)
if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
    print("Original List:", sample_list)
    print("\n--- Testing Shuffle ---")
    shuffle_names(sample_list)
    print("Shuffled List:", sample_list)
    sample_list_2 = ["Zoe", "Adam", "Beth", "Adam"]
    print("\nOriginal List 2:", sample_list_2)
    shuffle_names(sample_list_2)
    print("Shuffled List 2:", sample_list_2)
    print("\n--- Testing Sort ---")
    sort_names(sample_list)
    print("Sorted List:", sample_list)
    sample_list_3 = ["Charlie", "Alice", "Bob", "Charlie"]
    print("\nOriginal List 3:", sample_list_3)
    sort_names(sample_list_3)
    print("Sorted List 3:", sample_list_3)
    print("\n--- Testing Remove Duplicates ---")
    remove_duplicates(sample_list)
    print("List after removing duplicates (original list modified):", sample_list)
    sample_list_4 = ["Xavier", "Yara", "Xavier", "Zane", "Yara"]
    print("\nOriginal List 4:", sample_list_4)
    remove_duplicates(sample_list_4)
    print("List after removing duplicates (original list modified):", sample_list_4)