def are_numbers_different(num1, num2):
    yield num1 != num2

if __name__ == '__main__':
    sample_num1 = 5
    sample_num2 = 10
    generator = are_numbers_different(sample_num1, sample_num2)
    print(next(generator))