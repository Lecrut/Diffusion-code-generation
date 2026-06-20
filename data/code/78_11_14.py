def month_diff(start_month, end_month):
    return abs(end_month - start_month)

if __name__ == '__main__':
    print(month_diff(1, 5))
    print(month_diff(10, 3))
    print(month_diff(12, 12))