def compare_elements(data):
    val1 = data[0]
    val2 = data[5]
    return val1 > val2

if __name__ == '__main__':
    sample_list = [3, 7, 11, 15, 19, 23]
    print(f"Comparing list[{0}] ({sample_list[0]}) and list[{5}] ({sample_list[5]}): {compare_elements(sample_list)}")