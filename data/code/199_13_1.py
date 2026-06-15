import random
def shuffle_names(names):
    shuffled = names[:]
    random.shuffle(shuffled)
    return shuffled
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Original list:", sample_names)
    shuffled_list = shuffle_names(sample_names)
    print("Shuffled list:", shuffled_list)
    shuffled_list_2 = shuffle_names(sample_names)
    print("Another shuffle:", shuffled_list_2)