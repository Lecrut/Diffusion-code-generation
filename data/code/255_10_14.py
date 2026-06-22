MAX_VALUE = float('-inf')

def find_max_value(numbers):
    global MAX_VALUE
    if not numbers:
        return None
    for number in numbers:
        if number > MAX_VALUE:
            MAX_VALUE = number
    return MAX_VALUE
if __name__ == '__main__':
    sample_numbers = [10, 5, 22, 8, 30, 1]
    result = find_max_value(sample_numbers)
    print(result)