def index_generator(seq, item):
    for i, value in enumerate(seq):
        if value == item:
            yield i

def find_final_index(seq, item):
    return list(index_generator(seq, item))[-1] if item in seq else None

if __name__ == '__main__':
    sample_sequence = [1, 2, 3, 4, 2, 5, 2]
    target_item = 2
    final_index = find_final_index(sample_sequence, target_item)
    print(final_index)