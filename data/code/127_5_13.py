def is_odd(number):
    return number % 2 != 0

def odd_generator(numbers):
    return (num for num in numbers if is_odd(num))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    generator = odd_generator(sample_numbers)
    result = list(generator)
    print(result)