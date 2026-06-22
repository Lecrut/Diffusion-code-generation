def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    index = len(numbers) // 2
    return numbers[index]

if __name__ == '__main__':
    SAMPLE_LIST = [5, 15, 25, 35, 45]
    MIDDLE_ITEM = find_middle_item(SAMPLE_LIST)
    print(MIDDLE_ITEM)