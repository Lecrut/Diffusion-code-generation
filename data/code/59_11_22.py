def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    example_list = [15, 25, 35, 45, 55, 65]
    middle_value = find_middle_item(example_list)
    print(middle_value)