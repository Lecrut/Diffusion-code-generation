def is_odd(num):
    return num & 1

def find_odd_numbers(numbers):
    if not all(isinstance(n, int) for n in numbers):
        raise ValueError("All elements must be integers")
    return [num for num in numbers if is_odd(num)]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(find_odd_numbers(sample_values))