def get_middle_value(data_list):
    n = len(data_list)
    if n == 0:
        return None
    middle_index = n // 2
    if n % 2 == 1:
        return data_list[middle_index]
    else:
        return (data_list[middle_index - 1] + data_list[middle_index]) / 2

if __name__ == '__main__':
    sample_values = {
        "odd": [1, 2, 3, 4, 5],
        "even": [10, 20, 30, 40],
        "single": [99],
        "empty": []
    }
    
    for key, value in sample_values.items():
        print(f"Middle value of {value}: {get_middle_value(value)}")