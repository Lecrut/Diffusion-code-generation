def find_middle_element(data):
    if len(data) == 0:
        raise ValueError("Input sequence cannot be empty")
    mid_index = len(data) // 2
    return data[mid_index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    print(find_middle_element(sample_tuple))