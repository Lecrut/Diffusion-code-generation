def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    middle_index = len(numbers) // 2
    return numbers[middle_index]

if __name__ == '__main__':
    example_list = [5, 10, 15, 20, 25]
    print(find_middle_item(example_list))