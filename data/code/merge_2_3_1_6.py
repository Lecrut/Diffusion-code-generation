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
    sample_values = [10, -3.5, 'five', True]
    for value in sample_values:
        if not is_integer(value):
            print(f"{value} is not a valid integer.")
            continue
        parity_result = determine_parity(int(str(value)))
        print(f"The number {int(str(value))} has the following parity: {parity_result}.")