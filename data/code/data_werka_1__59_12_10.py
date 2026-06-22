def find_middle_item(numbers):
    if not numbers:
        return None
    index = len(numbers) // 2
    return numbers[index]

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    middle_value = find_middle_item(sample_values)
    print(middle_value)