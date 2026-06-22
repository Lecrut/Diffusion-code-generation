def add_two_numbers(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    sample_values = {'first_number': 7, 'second_number': 9}
    result = add_two_numbers(sample_values['first_number'], sample_values['second_number'])
    print(result)