def day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year % 100
    b = year // 100
    c = (1 + 5 * b + 4 * a + 6 * (a // 4) + day + ((month + 1) * 31 // 12)) % 7
    return ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][c]

if __name__ == '__main__':
    print(day_of_week(2024, 2, 29))