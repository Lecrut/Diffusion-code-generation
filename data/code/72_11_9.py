def compare_elements(data):
    val1 = data[0]
    val2 = data[5]
    return val1 > val2

if __name__ == '__main__':
    sample_list = [3, 6, 9, 12, 15, 18, 21]
    result = compare_elements(sample_list)
    print(f"Is list[{0}] ({sample_list[0]}) greater than list[{5}] ({sample_list[5]}): {result}")