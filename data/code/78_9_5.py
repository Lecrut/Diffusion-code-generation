def months_elapsed(start_month, end_month):
    return abs(end_month - start_month)
if __name__ == '__main__':
    print(months_elapsed(1, 5))
    print(months_elapsed(5, 1))
    print(months_elapsed(-3, 2))
    print(months_elapsed(2, -3))