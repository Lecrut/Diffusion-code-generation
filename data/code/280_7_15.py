def is_even(number):
    return number % 2 == 0

def print_number_type(number):
    if is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def repeat_action():
    for i in range(15):
        print_number_type(i)

if __name__ == '__main__':
    repeat_action()