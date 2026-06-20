MIDDLE_INDEX = lambda n: n // 2

def get_middle_element(numbers):
    if not numbers:
        raise ValueError("The list is empty.")
    return numbers[MIDDLE_INDEX(len(numbers))]

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    print(get_middle_element(sample_numbers))