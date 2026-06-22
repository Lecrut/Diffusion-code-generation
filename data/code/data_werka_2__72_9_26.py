def compare_elements(data, first_index, second_index):
    try:
        first_value = data[first_index]
    except IndexError:
        return "index out of bounds"
    try:
        second_value = data[second_index]
    except IndexError:
        return "index out of bounds"
    if first_value > second_value:
        return "greater than"
    if first_value < second_value:
        return "less than"
    return "equal"

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    outcome = compare_elements(sample_data, 0, 4)
    print(outcome)
    outcome2 = compare_elements(sample_data, 2, 2)
    print(outcome2)
    outcome3 = compare_elements(sample_data, 10, 1)
    print(outcome3)