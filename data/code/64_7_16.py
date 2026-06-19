def index_generator(sequence, item):
    for index, value in enumerate(sequence):
        if value == item:
            yield index

def find_final_index(sequence, item):
    generator = index_generator(sequence, item)
    try:
        while True:
            final_index = next(generator)
    except StopIteration:
        return final_index
    return None

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 2, 5, 2]
    target_item = 2
    print(find_final_index(sample_sequence, target_item))