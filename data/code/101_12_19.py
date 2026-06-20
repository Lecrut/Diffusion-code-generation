def zellers_congruence(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + (13 * (month + 1) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return f % 7

def get_day_of_week(year, month, day):
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[zellers_congruence(year, month, day)]

if __name__ == '__main__':
    print(get_day_of_week(1900, 1, 1))