def compare_elements(data, first_index, second_index):
    max_len = len(data)
    if not (0 <= first_index < max_len):
        return "index out of bounds"
    if not (0 <= second_index < max_len):
        return "index out of bounds"
    first_value = data[first_index]
    second_value = data[second_index]
    if first_value > second_value:
        return "greater than"
    if first_value < second_value:
        return "less than"
    return "equal"

if __name__ == '__main__':
    values = [5, 15, 10, 25]
    output = compare_elements(values, 0, 2)
    print(output)
    diff_output = compare_elements(values, 1, 3)
    print(diff_output)
    bound_output = compare_elements(values, 4, 0)
    print(bound_output)