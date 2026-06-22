def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    mid_index = len(numbers) // 2
    return numbers[mid_index]

if __name__ == '__main__':
    example_values = [10, 20, 30, 40, 50, 60]
    middle_element = find_middle_item(example_values)
    print(middle_element)