def access_elements(sample_list):
    indices = {
        'first': 0,
        'second': 1,
        'last': -1,
        'second_last': -2,
        'third_last': -3,
        'fourth_last': -4
    }
    return {key: sample_list[value] for key, value in indices.items()}

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45, 55, 65]
    result = access_elements(sample_data)
    print(result)