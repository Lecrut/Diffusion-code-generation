def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if __name__ == '__main__':
    for i in range(15):
        check_even_odd(i)