def check_even_odd(n):
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"

if __name__ == '__main__':
    for i in range(15):
        print(check_even_odd(i))