def filter_and_process_numbers(numbers):
    if not all(isinstance(num, int) and num >= 0 for num in numbers):
        raise ValueError("All elements in the list must be non-negative integers.")
    
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    sample_numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    filter_and_process_numbers(sample_numbers)