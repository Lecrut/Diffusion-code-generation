# Check if an integer is odd using the modulo operator: num % 2 != 0
def check_odd(num):
    return bool(num % 2)

if __name__ == '__main__':
    # Hard-coded sample value as requested (no user input allowed)
    number_to_check = 17
    result = check_odd(number_to_check)
    print(f"Is {number_to_check} odd? {result}")