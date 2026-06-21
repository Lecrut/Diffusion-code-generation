EMPTY_LIST_ERROR = 'The input list is empty'

def find_smallest_value(numbers):
    if not numbers:
        raise ValueError(EMPTY_LIST_ERROR)
    smallest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
    return smallest
if __name__ == '__main__':
    sample_values = [4, 2, 9, 7, 5, 6]
    print(find_smallest_value(sample_values))