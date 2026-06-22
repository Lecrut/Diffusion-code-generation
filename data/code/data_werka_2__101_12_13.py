def get_zeller_weekday(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return h

if __name__ == '__main__':
    result = get_zeller_weekday(1900, 1, 1)
    print(result)