DIVISORS = {'quarter': 4, 'century': 100, 'quadruple_century': 400}

def is_leap_year(year):
    q = DIVISORS['quarter']
    c = DIVISORS['century']
    qc = DIVISORS['quadruple_century']
    return year % qc == 0 or (year % q == 0 and year % c != 0)

if __name__ == '__main__':
    years_to_test = [2000, 1900, 2024, 2023, 2400, 2100, 1600, 1700]
    for y in years_to_test:
        print(f"{y}: {is_leap_year(y)}")