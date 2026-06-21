MAX_VALUES = 100000

def calculate_average(numbers):
    if not numbers:
        raise ValueError("Input list is empty")
    
    return sum(num for num in numbers) / len(numbers)

if __name__ == '__main__':
    test_numbers = [10, 20, 30, 40, 50]
    try:
        result1 = calculate_average(test_numbers)
        print(f"Average of {test_numbers}: {result1}")
    except ValueError as e:
        print(e)