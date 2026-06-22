def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    print(find_middle_item(sample_values))