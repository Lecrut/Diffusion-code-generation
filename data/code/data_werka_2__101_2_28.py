def get_day_of_week(year: int, month: int, day: int) -> str:
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if day < 1:
        raise ValueError("Invalid day")
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    names = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return names[h]

if __name__ == '__main__':
    print(get_day_of_week(2024, 2, 29))