def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25, 30]
    try:
        middle_value = find_middle_item(sample_data)
        print(middle_value)
    except ValueError as e:
        print(e)