def get_numbers():
    """Returns two integers to compare."""
    return 10, 25

if __name__ == '__main__':
    num1, num2 = get_numbers()
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")