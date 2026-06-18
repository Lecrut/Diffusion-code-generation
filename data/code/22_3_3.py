num = 17
is_odd = num % 2 != 0 if isinstance(num, int) else False
if __name__ == '__main__':
    print(f"{num} is odd: {is_odd}")