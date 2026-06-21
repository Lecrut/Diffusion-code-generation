SAMPLE_DATA = [10, 20, 30, 40, 50]

def get_last_element(sequence):
    length = len(sequence)
    return sequence[length - 1]

if __name__ == '__main__':
    sample_list = SAMPLE_DATA
    result = get_last_element(sample_list)
    print(result)