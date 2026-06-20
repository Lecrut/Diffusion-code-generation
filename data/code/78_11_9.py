def months_elapsed(start_month, end_month):
    return abs(end_month - start_month)

if __name__ == '__main__':
    print(months_elapsed(1, 5))
    print(months_elapsed(10, 3))
    print(months_elapsed(12, 12))