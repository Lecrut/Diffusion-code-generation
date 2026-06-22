def get_day_index(year, month, day):
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError("Arguments must be integers")
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")
    if day < 1 or day > 31:
        raise ValueError("Day must be valid for the month")
    if year < 1:
        raise ValueError("Year must be positive")
    if month == 1 or month == 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h

def get_weekday_name(index):
    names = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    return names[index]

if __name__ == '__main__':
    target_year = 1900
    target_month = 1
    target_day = 1
    index = get_day_index(target_year, target_month, target_day)
    name = get_weekday_name(index)
    print(name)