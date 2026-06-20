def check_range(a, b, c):
    return (a >= 0 and a <= 10) and (b >= 0 and b <= 10) and (c >= 0 and c <= 10)

if __name__ == '__main__':
    print(check_range(5, 7, 9))