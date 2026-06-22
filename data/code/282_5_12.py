def sum_with_generator(numbers):
    return sum(x for x in numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = sum_with_generator(sample_numbers)
    print(result)