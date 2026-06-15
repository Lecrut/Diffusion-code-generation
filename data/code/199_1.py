import random
def shuffle_names(names):
    shuffled = list(names)
    random.shuffle(shuffled)
    return shuffled
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona", "George", "Hannah"]
    shuffled_list = shuffle_names(sample_names)
    print(shuffled_list)