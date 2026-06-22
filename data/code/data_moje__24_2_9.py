def is_leap(year):
    div4 = year % 4 == 0
    div100 = year % 100 == 0
    div400 = year % 400 == 0
    return div4 and (not div100 or div400)

if __name__ == '__main__':
    y1 = 2004
    y2 = 1900
    y3 = 2000
    print(is_leap(y1))
    print(is_leap(y2))
    print(is_leap(y3))