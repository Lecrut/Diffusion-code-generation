def find_middle_item(numbers):
    if not numbers:
        return None
    index = len(numbers) // 2
    return numbers[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    middle_value = find_middle_item(sample_list)
    print(middle_value)