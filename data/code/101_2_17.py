def day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year % 100
    b = year // 100
    c = (1 + ((5 * b) // 4)) + a + (a // 4) + ((26 * (month + 1)) // 10)
    day_of_week = (c + day) % 7
    return ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'][day_of_week]

if __name__ == '__main__':
    print(day_of_week(2024, 2, 29))