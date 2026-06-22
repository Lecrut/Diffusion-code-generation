def find_minimum(int_list):
    current_min = int_list[0]
    for num in int_list[1:]:
        if num < current_min:
            current_min = num
    return current_min

if __name__ == '__main__':
    sample_values = [3, 1, 4, 1, 5, 9, 2, 6]
    result = find_minimum(sample_values)
    print(result)