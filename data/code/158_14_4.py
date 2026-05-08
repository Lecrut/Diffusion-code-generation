def check_even_odd(number):
    if isinstance(number, int):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    else:
        print("Invalid input. Please enter an integer.")
if __name__ == '__main__':
    sample_inputs = [42, 17, 0, -5, "hello", 3.14]
    for input_value in sample_inputs:
        check_even_odd(input_value)