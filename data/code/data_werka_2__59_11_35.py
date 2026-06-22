MIDDLE_INDEX_FACTOR = 2

def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    index = len(numbers) // MIDDLE_INDEX_FACTOR
    return numbers[index]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    middle_element = find_middle_item(sample_data)
    print(middle_element)