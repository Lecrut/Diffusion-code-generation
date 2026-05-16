def check_even_odd(number):
    if isinstance(number, int):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    else:
        print("Error: Input must be an integer.")
if __name__ == '__main__':
    sample_values = [4, 7, 0, -3, 12]
    for value in sample_values:
        check_even_odd(value)