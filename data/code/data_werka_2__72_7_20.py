def is_first_element_leq_second(list_a, list_b, index):
    if index < 0:
        raise ValueError("Index cannot be negative")
    if index >= len(list_a):
        raise ValueError("Index out of range for first list")
    if index >= len(list_b):
        raise ValueError("Index out of range for second list")
    first_value = list_a[index]
    second_value = list_b[index]
    return first_value <= second_value

if __name__ == '__main__':
    values_one = [1, 2, 3]
    values_two = [4, 5, 6]
    target_index = 2
    output = is_first_element_leq_second(values_one, values_two, target_index)
    print(output)