def shuffle_names(names):
    import random
    random.shuffle(names)
def sort_names(names):
    names.sort()
def remove_duplicates(names):
    unique_names = []
    for name in names:
        if name not in unique_names:
            unique_names.append(name)
    names[:] = unique_names
if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]
    print("Original List:", sample_list)
    print("\n--- Testing Shuffle ---")
    shuffle_names(sample_list)
    print("Shuffled List:", sample_list)
    unsorted_list = ["Zoe", "Adam", "Ben", "Charlie"]
    print("\n--- Testing Sort ---")
    print("Original Unsorted List:", unsorted_list)
    sort_names(unsorted_list)
    print("Sorted List:", unsorted_list)
    duplicate_list = ["Anna", "Ben", "Anna", "Cathy", "Ben"]
    print("\n--- Testing Remove Duplicates ---")
    print("List with Duplicates:", duplicate_list)
    remove_duplicates(duplicate_list)
    print("List without Duplicates:", duplicate_list)