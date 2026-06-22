def compute_zeller_day(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    century = year // 100
    year_in_century = year % 100
    term1 = day
    term2 = (13 * (month + 1)) // 5
    term3 = year_in_century
    term4 = year_in_century // 4
    term5 = century // 4
    term6 = 2 * century
    h = (term1 + term2 + term3 + term4 + term5 - term6) % 7
    return h

if __name__ == '__main__':
    result = compute_zeller_day(2023, 10, 25)
    print(result)