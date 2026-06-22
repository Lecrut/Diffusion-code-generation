def access_elements(sample_list):
    indices = {
        'first': 0,
        'second': 1,
        'last': -1,
        'second_last': -2,
        'third_last': -3,
        'fourth_last': -4
    }
    
    result = {key: sample_list[value] for key, value in indices.items() if len(sample_list) > abs(value)}
    return result

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 60]
    result = access_elements(sample_data)
    print(result)