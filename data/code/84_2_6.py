def day_of_year(year, month, day):
    m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return (year - 1) * 365 + year // 4 - year // 100 + year // 400 + sum(m[:month]) + day

if __name__ == '__main__':
    print(day_of_year(2023, 10, 27))