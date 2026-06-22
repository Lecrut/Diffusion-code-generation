def is_valid_list(lst):
    return isinstance(lst, list) and all(isinstance(x, float) for x in lst)

def calculate_median(numbers):
    if not is_valid_list(numbers):
        raise ValueError("Input must be a list of floats")
    
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2.0
    else:
        return float(numbers[mid])

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9, 5.1]
    print(calculate_median(sample_values))