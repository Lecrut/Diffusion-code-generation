def analyze_numbers(numbers):
    odd_count = 0
    for num in numbers:
        if num % 2 != 0:
            odd_count += 1
    if odd_count % 2 == 0:
        print("The count of odd numbers is even.")
    else:
        print("The count of odd numbers is odd.")
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    analyze_numbers(sample_numbers)