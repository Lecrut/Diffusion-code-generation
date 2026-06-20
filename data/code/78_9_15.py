def months_between(start_month: int, end_month: int) -> int:
    return abs(end_month - start_month)
if __name__ == '__main__':
    print(months_between(3, 9))
    print(months_between(12, 4))
    print(months_between(-3, -9))
    print(months_between(-12, -4))