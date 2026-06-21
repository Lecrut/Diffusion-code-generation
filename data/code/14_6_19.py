def get_third_element_negative_index(sequence):
    lookup_map = {
        'third_from_end': -3,
        'second_from_end': -2,
        'last': -1
    }
    index_key = 'third_from_end'
    target_index = lookup_map[index_key]
    return sequence[target_index]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    result = get_third_element_negative_index(sample_data)
    print(result)