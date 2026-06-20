def validate_input(numbers):
    if not isinstance(numbers, list) or not all(isinstance(num, int) for num in numbers):
        raise ValueError("Input must be a list of integers")

def partition_sort(numbers):
    validate_input(numbers)
    evens = sorted([num for num in numbers if num % 2 == 0])
    odds = sorted([num for num in numbers if num % 2 != 0])
    return evens, odds

if __name__ == '__main__':
    sample_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    even_list, odd_list = partition_sort(sample_numbers)
    print("Even numbers:", even_list)
    print("Odd numbers:", odd_list)