def get_odd_numbers(numbers):
    return (num for num in numbers if num % 2 != 0)
if __name__ == '__main__':
    sample_data = [1, 4, 7, 8, 9, 15, 22]
    odd_generator = get_odd_numbers(sample_data)
    for number in odd_generator:
        print(number)