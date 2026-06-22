def calculate_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]

if __name__ == '__main__':
    result = calculate_day_of_week(2024, 2, 29)
    print(result)