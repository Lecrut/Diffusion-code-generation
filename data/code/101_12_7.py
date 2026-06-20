def zellers_congruence(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    f = day + (13 * (month + 1) // 5) + k + (k // 4) + (j // 4) - (2 * j)
    return f % 7

if __name__ == '__main__':
    print(zellers_congruence(1900, 1, 1))