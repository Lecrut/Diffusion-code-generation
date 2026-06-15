def shuffle_names(names):
    import random
    random.shuffle(names)
def sort_names(names):
    names.sort()
def remove_duplicates(names):
    unique_names = set(names)
    names[:] = list(unique_names)
if __name__ == '__main__':
    sample_list = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]
    print("Original List:", sample_list)
    shuffled_list = list(sample_list)
    shuffle_names(shuffled_list)
    print("Shuffled List:", shuffled_list)
    sorted_list = list(sample_list)
    sort_names(sorted_list)
    print("Sorted List:", sorted_list)
    duplicates_list = ["Anna", "Ben", "Anna", "Cathy", "Ben"]
    print("\nOriginal Duplicates List:", duplicates_list)
    remove_duplicates(duplicates_list)
    print("List after removing duplicates:", duplicates_list)