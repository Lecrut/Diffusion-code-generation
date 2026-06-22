numbers = [1, 2, 3, 4, 5]

def print_numbers_ten_times(numbers):
    if not isinstance(numbers, list) or not all(isinstance(n, int) for n in numbers):
        raise ValueError("Input must be a list of integers")
    
    repetitions = 10
    for number in numbers:
        for _ in range(repetitions):
            print(number)

if __name__ == '__main__':
    try:
        print_numbers_ten_times(numbers)
    except ValueError as e:
        print(e)