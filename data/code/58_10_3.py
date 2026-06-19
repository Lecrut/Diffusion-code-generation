def fetch_initial_element(sequence):
    return sequence[0] if sequence else None

if __name__ == '__main__':
    example_list = [7, 14, 21, 28, 35]
    print(fetch_initial_element(example_list))