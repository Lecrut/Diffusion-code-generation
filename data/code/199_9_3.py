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
    sorted_list = ["Zoe", "Adam", "Ben"]
    print("\n--- Testing Sort ---")
    print("Before Sorting:", sorted_list)
    sort_names(sorted_list)
    print("After Sorting:", sorted_list)
    duplicate_list = ["A", "B", "C", "A", "D", "B"]
    print("\n--- Testing Remove Duplicates ---")
    print("Before Removing Duplicates:", duplicate_list)
    remove_duplicates(duplicate_list)
    print("After Removing Duplicates:", duplicate_list)