def find_month_difference(month1, month2):
    return abs(month1 - month2)

if __name__ == '__main__':
    print(find_month_difference(1, 5))
    print(find_month_difference(12, 3))
    print(find_month_difference(7, 7))