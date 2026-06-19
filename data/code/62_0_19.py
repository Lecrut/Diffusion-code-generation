def fetch_second_element(sequence):
    return sequence[1]

if __name__ == '__main__':
    example_list = [5, 15, 25, 35, 45]
    index_of_interest = 1
    second_element = fetch_second_element(example_list)
    print(second_element)