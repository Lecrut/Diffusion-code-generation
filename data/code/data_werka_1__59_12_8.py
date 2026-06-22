def find_middle_item(numbers):
    if not numbers:
        return None
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 9]
    print(find_middle_item(sample_values))