LAST_INDEX_NEGATIVE = -1

def retrieve_final_item(sequence):
    return sequence[LAST_INDEX_NEGATIVE]

if __name__ == '__main__':
    data_set = [1, 2, 3, 4, 5]
    final_value = retrieve_final_item(data_set)
    print(final_value)