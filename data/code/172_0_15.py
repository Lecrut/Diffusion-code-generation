def map_integers_to_strings(input_dict):
    return {key: str(value) for key, value in input_dict.items()}

if __name__ == '__main__':
    sample_dict = {1: 2, 3: 4, 5: 6}
    result = map_integers_to_strings(sample_dict)
    print(result)