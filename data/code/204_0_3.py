import statistics

def find_middle_value(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers")
    
    return statistics.median(numbers)

if __name__ == '__main__':
    sample_values = [1, 5, 2, 8, 3]
    try:
        print(find_middle_value(sample_values))
    except ValueError as e:
        print(e)