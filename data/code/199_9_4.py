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
    shuffled_list = list(sample_list)
    shuffle_names(shuffled_list)
    print("Shuffled List:", shuffled_list)
    sorted_list = list(sample_list)
    sort_names(sorted_list)
    print("Sorted List:", sorted_list)
    duplicates_list = list(sample_list)
    remove_duplicates(duplicates_list)
    print("List with Duplicates Removed:", duplicates_list)