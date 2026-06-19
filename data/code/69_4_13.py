def validate_list_and_index(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError('Error: Input must be a list.')
    if not isinstance(index, int):
        raise TypeError('Error: Index must be an integer.')
    if index < 0 or index >= len(data_list):
        raise IndexError('Error: Index out of bounds.')

def extract_second_elements(data_list):
    try:
        validate_list_and_index(data_list, 0)
        return [data_list[i] for i in range(1, len(data_list), 2)]
    except (TypeError, IndexError) as e:
        print(e)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print('Extracting every second element from the list:')
    result = extract_second_elements(sample_list)
    if result is not None:
        print(result)