def is_zero(number):
    return number == 0

if __name__ == '__main__':
    sample_values = [0, 5, -3, 0]
    for value in sample_values:
        result = is_zero(value)
        print(f"Checking value: {value}, Is zero: {result}")