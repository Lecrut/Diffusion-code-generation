import sys
def check_even_odd(number):
    if isinstance(number, int):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
    else:
        print("Error: Input must be an integer.")
if __name__ == '__main__':
    sample_inputs = [42, 7, 0, -15, "hello", 3.14]
    for input_val in sample_inputs:
        check_even_odd(input_val)