INDEX_OFFSET = -1

def get_last_element(sequence):
    return sequence[INDEX_OFFSET]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25]
    output = get_last_element(sample_data)
    print(output)