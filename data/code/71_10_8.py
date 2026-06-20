def find_middle_element(data):
    n = len(data)
    middle_index = (n - 1) // 2
    return data[middle_index]

if __name__ == '__main__':
    sample_list = [7, 3, 5, 9, 1]
    print(f"Middle element of {sample_list}: {find_middle_element(sample_list)}")