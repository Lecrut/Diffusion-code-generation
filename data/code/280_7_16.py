def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == '__main__':
    for i in range(15):
        result = check_even_odd(i)
        print(f"{i} is {result}")