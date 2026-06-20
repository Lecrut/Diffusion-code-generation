def months_elapsed(start_month, end_month):
    return abs(end_month - start_month)
if __name__ == '__main__':
    print(months_elapsed(3, 9))
    print(months_elapsed(12, 4))
    print(months_elapsed(-5, -1))