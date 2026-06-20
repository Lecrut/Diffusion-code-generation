def calculate_day_of_week(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    a = year % 100
    b = year // 100
    q = month
    h = (q + ((13 * (q + 1)) // 5) + a + (a // 4) + (b // 4) - (2 * b)) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

if __name__ == '__main__':
    print(calculate_day_of_week(2024, 2, 29))