def find_max_element(two_d_array):
    if not two_d_array:
        return None
    max_element = float('-inf')
    for sub_array in two_d_array:
        if sub_array:
            current_max = max(sub_array)
            if current_max > max_element:
                max_element = current_max
    return max_element
if __name__ == '__main__':
    input_data = [[10, 5, 20], [8, 15], [], [9]]
    result = find_max_element(input_data)
    print(result)