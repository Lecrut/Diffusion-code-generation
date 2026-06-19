def index_generator(sequence, item):
    for index, value in enumerate(sequence):
        if value == item:
            yield index

def find_final_index(sequence, item):
    final_index = None
    for index in index_generator(sequence, item):
        final_index = index
    return final_index

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 2, 5, 2]
    target_item = 2
    print(find_final_index(sample_sequence, target_item))