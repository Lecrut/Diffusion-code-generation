def compare_elements(data, first_index, second_index):
    list_length = len(data)
    if not (0 <= first_index < list_length):
        return "index out of bounds"
    if not (0 <= second_index < list_length):
        return "index out of bounds"
    element_one = data[first_index]
    element_two = data[second_index]
    difference = element_one - element_two
    if difference > 0:
        return "greater than"
    if difference < 0:
        return "less than"
    return "equal"

if __name__ == '__main__':
    test_data = [5, 15, 25, 35, 45]
    index_a = 0
    index_b = 4
    outcome = compare_elements(test_data, index_a, index_b)
    print(outcome)
    boundary_outcome = compare_elements(test_data, 5, 0)
    print(boundary_outcome)