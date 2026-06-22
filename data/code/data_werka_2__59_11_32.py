def find_middle_item(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if len(numbers) == 0:
        raise ValueError("The list is empty")
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        middle_item = find_middle_item(sample_list)
        print(middle_item)
    except Exception as e:
        print(f"Error: {e}")