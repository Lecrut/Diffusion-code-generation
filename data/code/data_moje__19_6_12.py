import random

MIN_VALID_INDEX = 0

def select_random_from_collection(collection_set):
    if not collection_set:
        return None
    converted_sequence = list(collection_set)
    sequence_size = len(converted_sequence)
    chosen_pos = random.randint(MIN_VALID_INDEX, sequence_size - 1)
    return converted_sequence[chosen_pos]

if __name__ == '__main__':
    data_pool = {'red', 'green', 'blue', 'yellow'}
    picked_item = select_random_from_collection(data_pool)
    print(picked_item)