def day_of_year(y, m, d):
    return 365 * (y - 1) + (m - 1) * 30 + d
if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))