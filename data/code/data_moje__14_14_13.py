LIST_INDEX = 2
SAMPLE_DATA = [99, 88, 77, 66, 55]

def retrieve_item_at_index(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    target = retrieve_item_at_index(SAMPLE_DATA, LIST_INDEX)
    print(target)