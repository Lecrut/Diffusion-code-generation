def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for element in data[1:]:
        if element < minimum:
            minimum = element
    return minimum

if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    sample_data2 = [-10, 0, 5, -3]
    sample_data3 = [42]
    print(f"Minimum of {sample_data1}: {find_minimum(sample_data1)}")
    print(f"Minimum of {sample_data2}: {find_minimum(sample_data2)}")
    print(f"Minimum of {sample_data3}: {find_minimum(sample_data3)}")