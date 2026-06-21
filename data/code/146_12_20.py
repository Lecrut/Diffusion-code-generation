def process_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            continue
        if number > 50:
            break
        print(number)

if __name__ == '__main__':
    sample_values = [1, 3, 5, 7, 8, 10, 12, 45, 55, 60]
    process_numbers(sample_values)