def is_even(number: int) -> bool:
    return number % 2 == 0

if __name__ == '__main__':
    values = [-3, -2, 0, 4, 9]
    for val in values:
        result = is_even(val)
        print(result)