def find_largest_number(data_list):
    float_values = [float(item) for item in data_list]
    return max(float_values)

if __name__ == '__main__':
    sample_data1 = [10, 5, 20.5, '8', -3]
    sample_data2 = [-5, -1.1, -10, '3']
    sample_data3 = [42, '42.0']

    result1 = find_largest_number(sample_data1)
    print(f"Maximum of {sample_data1}: {result1}")

    result2 = find_largest_number(sample_data2)
    print(f"Maximum of {sample_data2}: {result2}")

    result3 = find_largest_number(sample_data3)
    print(f"Maximum of {sample_data3}: {result3}")