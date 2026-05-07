def day_of_year(y, m, d):
    return 365 * (y - 1) + (m // 12) * 30 + d - (m % 12) * 1 if m > 2 else 365 * (y - 1) + m * 30 + d
if __name__ == '__main__':
    print(day_of_year(2023, 10, 26))