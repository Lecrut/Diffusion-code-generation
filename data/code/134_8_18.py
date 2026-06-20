TRUE = 1
FALSE = 0

def count_and_check_exclusive(a, b, c, d, e):
    count = (a << 4) | (b << 3) | (c << 2) | (d << 1) | e
    return (count & (count - 1)) == FALSE

if __name__ == '__main__':
    result = count_and_check_exclusive(TRUE, FALSE, TRUE, FALSE, FALSE)
    print(result)