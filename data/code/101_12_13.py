def zellers_congruence(year, month, day):
    if month < 3:
        year -= 1
        month += 12
    q = day
    m = month
    K = year % 100
    J = year // 100
    f = q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) - (2 * J)
    return f % 7

if __name__ == '__main__':
    print(zellers_congruence(1900, 1, 1))