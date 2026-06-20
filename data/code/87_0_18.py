def combine_conditions(numbers):
    return all(x > 0 and x % 2 == 0 for x in numbers)

if __name__ == '__main__':
    sample_numbers = [4, 6, 8, 10]
    result = combine_conditions(sample_numbers)
    print(result)