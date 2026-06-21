def find_odd_numbers(numbers):
    return [num for num in numbers if num & 1]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = find_odd_numbers(sample_numbers)
    print(odd_numbers)