NUMBERS = [1, 2, 3, 4, 5]

def square_numbers(numbers):
    return [x**2 for x in numbers]

if __name__ == '__main__':
    squared_result = square_numbers(NUMBERS)
    print(squared_result)