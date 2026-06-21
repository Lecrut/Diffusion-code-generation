def compare_elements(data, first_idx, second_idx):
    list_length = len(data)
    if not (0 <= first_idx < list_length):
        return "index out of bounds"
    if not (0 <= second_idx < list_length):
        return "index out of bounds"
    target_value_one = data[first_idx]
    target_value_two = data[second_idx]
    if target_value_one > target_value_two:
        return "greater than"
    if target_value_one < target_value_two:
        return "less than"
    return "equal"

if __name__ == '__main__':
    numbers = [100, 200, 150, 50, 75]
    output = compare_elements(numbers, 2, 4)
    print(output)