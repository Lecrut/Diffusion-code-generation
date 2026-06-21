def is_even(number):
    return number % 2 == 0

def process_numbers(numbers):
    for number in numbers:
        if number > 50:
            break
        if is_even(number):
            continue
        print(number)

if __name__ == '__main__':
    sample_numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    process_numbers(sample_numbers)