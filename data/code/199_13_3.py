import random
def shuffle_names(names):
    shuffled_list = list(names)
    random.shuffle(shuffled_list)
    return shuffled_list
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Original list:", sample_names)
    shuffled_names = shuffle_names(sample_names)
    print("Shuffled list:", shuffled_names)
    shuffled_names_2 = shuffle_names(sample_names)
    print("Another shuffled list:", shuffled_names_2)