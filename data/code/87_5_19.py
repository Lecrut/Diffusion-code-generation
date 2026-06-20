def check_even_greater_than_fifty(numbers):
    criteria = {
        'even': lambda x: x % 2 == 0,
        'greater_than_fifty': lambda x: x > 50
    }
    return any(criteria['even'](num) and criteria['greater_than_fifty'](num) for num in numbers)

if __name__ == '__main__':
    sample_numbers = [45, 60, 75, 80]
    print(check_even_greater_than_fifty(sample_numbers))