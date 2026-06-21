def filter_and_process(numbers):
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        print(number)

if __name__ == '__main__':
    sample_numbers = [14, 37, 59, 61, 88]
    filter_and_process(sample_numbers)