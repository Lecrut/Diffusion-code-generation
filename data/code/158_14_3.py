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
    sample_inputs = [42, 17, 0, -5, "hello"]
    for num in sample_inputs:
        check_even_odd(num)