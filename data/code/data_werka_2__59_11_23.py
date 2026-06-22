def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    return numbers[len(numbers) // 2]

if __name__ == '__main__':
    test_list = [100, 200, 300, 400, 500]
    print(find_middle_item(test_list))