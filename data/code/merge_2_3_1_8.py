def is_integer(value):
    try:
        int(str(value))
        return True
    except (ValueError, TypeError):
        return False
def get_parity(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
if __name__ == '__main__':
    test_values = [42, -7, '15', None]
    for val in test_values:
        if not is_integer(val):
            print(f"{val} is not a valid integer.")
        else:
            parity = get_parity(int(val))
            print(f"The number {int(val)} has the following parity: {parity}.")