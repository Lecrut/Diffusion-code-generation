def day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year // 100
    b = year % 100
    c = (a // 4) - a + b + (b // 4) + (5 * a) + (26 * (month + 1) // 10) + day
    return (c % 7)

if __name__ == '__main__':
    print(day_of_week(2024, 2, 29))