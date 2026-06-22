MIDDLE_INDEX_CONSTANT = 2

def find_middle_item(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    index = len(numbers) // MIDDLE_INDEX_CONSTANT
    return numbers[index]

if __name__ == '__main__':
    sample_data = [5, 10, 15, 20, 25, 30]
    middle_element = find_middle_item(sample_data)
    print(middle_element)