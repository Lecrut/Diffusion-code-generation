def zellers_congruence(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    K = year % 100
    J = year // 100
    f = day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return f % 7

def get_day_name(day):
    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days_of_week[day]

if __name__ == '__main__':
    year = 1900
    month = 1
    day = 1
    day_of_week_index = zellers_congruence(year, month, day)
    day_name = get_day_name(day_of_week_index)
    print(f"January 1, 1900 was a {day_name}")