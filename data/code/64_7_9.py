def index_generator(sequence, item):
    for index, value in enumerate(sequence):
        if value == item:
            yield index

def find_final_index(sequence, item):
    return list(index_generator(sequence, item))[-1] if any(index_generator(sequence, item)) else None

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 2, 5, 2]
    target_item = 2
    final_index = find_final_index(sample_sequence, target_item)
    print(final_index)