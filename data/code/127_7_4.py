def analyze_numbers(numbers):
    odd_count = 0
    for num in numbers:
        if num % 2 != 0:
            odd_count += 1
    if odd_count % 2 == 0:
        print("Even number of odd numbers.")
    else:
        print("Odd number of odd numbers.")
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    analyze_numbers(sample_numbers)