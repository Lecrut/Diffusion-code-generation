def fetch_last_element(sequence):
    return sequence[-1]

if __name__ == '__main__':
    sample_data = {'list': [1, 2, 3, 4, 5], 'tuple': (6, 7, 8, 9, 10)}
    print(fetch_last_element(sample_data['list']))