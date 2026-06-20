def check_range(a, b, c):
    return (a >= 0 and a <= 10) and (b >= 0 and b <= 20) and (c >= 0 and c <= 30)

if __name__ == '__main__':
    print(check_range(5, 15, 25))