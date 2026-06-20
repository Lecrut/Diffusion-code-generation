def is_negative(number):
    return number < 0

if __name__ == '__main__':
    test_values = [-5.0, 123, -789.10]
    for value in test_values:
        result = is_negative(value)
        print(f"is_negative({value}) -> {result}")