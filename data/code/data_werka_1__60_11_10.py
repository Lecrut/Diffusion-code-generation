LAST_ITEM_INDEX = -1

def fetch_final_element(sequence):
    return sequence[LAST_ITEM_INDEX]

if __name__ == '__main__':
    sample_sequence = [100, 200, 300, 400, 500]
    print(fetch_final_element(sample_sequence))