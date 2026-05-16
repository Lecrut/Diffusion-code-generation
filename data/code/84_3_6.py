def day_of_year(y, m, d):
    return 365 * (y - 1) + (m - 1) * 30.4375 + d + (y // 4) - (y // 100) + (y // 400)
if __name__ == '__main__':
    print(day_of_year(2023, 10, 26))