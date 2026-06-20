def is_number_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    num1 = -3
    num2 = 4
    num3 = -7
    num4 = 6
    print(f"num1: {is_number_odd(num1)}")
    print(f"num2: {is_number_odd(num2)}")
    print(f"num3: {is_number_odd(num3)}")
    print(f"num4: {is_number_odd(num4)}")