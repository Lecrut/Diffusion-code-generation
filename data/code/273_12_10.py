def double_evens(numbers):
    return [num for num in numbers if num % 2 == 0] * 2

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    doubled_evens = double_evens(sample_numbers)
    print(doubled_evens)