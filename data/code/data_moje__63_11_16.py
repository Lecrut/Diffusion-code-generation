def reverse_integer(n):
    if n < 0:
        return -int(str(-n)[::-1])
    return int(str(n)[::-1])

if __name__ == '__main__':
    test_cases = [
        123,
        -456,
        1200,
        -10,
        0,
        7,
        -999
    ]
    for tc in test_cases:
        print(reverse_integer(tc))