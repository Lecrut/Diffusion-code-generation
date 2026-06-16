def is_integer(value):
    try:
        int(str(value))
        return True
    except (ValueError, TypeError):
        return False
def determine_parity(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
if __name__ == '__main__':
    sample_values = [1, -5, "three", None]
    for value in sample_values:
        if not isinstance(value, int):
            continue
        if is_integer(value):
            determine_parity(value)
        else:
            print(f"{value} cannot be processed.")