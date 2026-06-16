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
    test_values = [1, -5, "abc", None]
    for val in test_values:
        if not isinstance(val, (int, float)) and not str(val).lstrip('-').isdigit():
            continue
        try:
            num = int(val)
            if is_integer(num):
                determine_parity(num)
            else:
                print(f"{val} cannot be processed as an integer.")
        except Exception:
            print(f"Error processing {val}.")