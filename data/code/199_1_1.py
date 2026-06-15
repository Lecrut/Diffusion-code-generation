import random
def shuffle_names(names):
    shuffled = list(names)
    random.shuffle(shuffled)
    return shuffled
if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve", "Fiona", "George", "Hannah"]
    shuffled_list = shuffle_names(sample_names)
    print(f"Original list: {sample_names}")
    print(f"Shuffled list: {shuffled_list}")
    sample_names_2 = ["A", "B", "C", "D", "E"]
    shuffled_list_2 = shuffle_names(sample_names_2)
    print(f"Original list: {sample_names_2}")
    print(f"Shuffled list: {shuffled_list_2}")