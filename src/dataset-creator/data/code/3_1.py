def is_integer(value):
    try:
        int(str(value))
        return True
    except (ValueError, TypeError):
        return False
def determine_parity(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    sample_values = [10, -3.5, 'abc', True]
    for value in sample_values:
        if is_integer(value):
            parity_result = determine_parity(int(str(value)))
            print(f"{value} is {parity_result}")
        else:
            print(f"Invalid input: {value}")