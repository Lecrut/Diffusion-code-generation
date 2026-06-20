def day_of_year(year, month, day):
    return (year - 1900) * 365 + sum([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:month-1]) + day

if __name__ == '__main__':
    print(day_of_year(2023, 4, 15))