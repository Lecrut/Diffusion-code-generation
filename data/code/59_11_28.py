def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return numbers[len(numbers) // 2]

if __name__ == '__main__':
    sample_numbers = [7, 14, 21, 28, 35, 42]
    middle_number = find_middle_item(sample_numbers)
    print(middle_number)