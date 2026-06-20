def is_number_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    print(f"1: {is_number_odd(1)}")
    print(f"-1: {is_number_odd(-1)}")
    print(f"2: {is_number_odd(2)}")
    print(f"-2: {is_number_odd(-2)}")
    print(f"0: {is_number_odd(0)}")