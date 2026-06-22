def get_day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    q = day
    m = month
    k = year % 100
    j = year // 100
    h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h
if __name__ == '__main__':
    day_of_week = get_day_of_week(1900, 1, 1)
    print(day_of_week)