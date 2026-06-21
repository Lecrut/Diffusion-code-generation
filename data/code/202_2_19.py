MAX_VALUE = float('-inf')

def find_maximum(numbers):
    global MAX_VALUE
    if not numbers:
        raise ValueError("The list of numbers is empty")
    for number in numbers:
        if number > MAX_VALUE:
            MAX_VALUE = number
    return MAX_VALUE

if __name__ == '__main__':
    sample_numbers = [15, 8, 42, 3, 99, 27]
    max_number = find_maximum(sample_numbers)
    print(max_number)