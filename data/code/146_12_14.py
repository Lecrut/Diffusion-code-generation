def filter_and_stop(numbers):
    for number in numbers:
        if number > 50:
            break
        if number % 2 == 0:
            continue
        yield number

if __name__ == '__main__':
    sample_numbers = [3, 5, 8, 10, 23, 45, 60, 70]
    filtered_numbers = list(filter_and_stop(sample_numbers))
    for num in filtered_numbers:
        print(num)