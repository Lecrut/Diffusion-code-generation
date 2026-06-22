def is_even(number):
    return number % 2 == 0

def print_number_type(i):
    if is_even(i):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

if __name__ == '__main__':
    for i in range(15):
        print_number_type(i)