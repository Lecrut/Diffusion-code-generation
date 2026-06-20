def is_odd(number):
    return number & 1

def analyze_numbers(numbers):
    odd_count = sum(is_odd(num) for num in numbers)
    if odd_count % 2 == 0:
        print("The collection has an even count of odd numbers.")
    else:
        print("The collection has an odd count of odd numbers.")

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    analyze_numbers(sample_numbers)