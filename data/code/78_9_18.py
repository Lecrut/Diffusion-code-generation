def months_elapsed(start_month: int, end_month: int) -> int:
    return abs(end_month - start_month)

if __name__ == '__main__':
    print(months_elapsed(5, 10))
    print(months_elapsed(10, 5))
    print(months_elapsed(-3, -9))
    print(months_elapsed(-9, -3))