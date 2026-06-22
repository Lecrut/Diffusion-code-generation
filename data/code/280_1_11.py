NUMBERS_TO_APPEND = list(range(1, 6))

def append_numbers(numbers: list):
    numbers.extend(NUMBERS_TO_APPEND)
    return numbers

if __name__ == '__main__':
    result = append_numbers([])
    print(result)