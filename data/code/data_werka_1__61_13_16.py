def fetch_element(sequence, index):
    return sequence[index]

if __name__ == '__main__':
    SAMPLE_INDEX = 2

    sample_list = [100, 200, 300, 400, 500]
    sample_tuple = ('alpha', 'beta', 'gamma', 'delta', 'epsilon')

    print(fetch_element(sample_list, SAMPLE_INDEX))
    print(fetch_element(sample_tuple, SAMPLE_INDEX))