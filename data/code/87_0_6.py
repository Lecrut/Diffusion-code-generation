def combine_conditions(numbers):
    return all(x > 0 for x in numbers) and any(x % 2 == 0 for x in numbers)

if __name__ == '__main__':
    sample_numbers = [4, -1, 2, 5]
    print(combine_conditions(sample_numbers))