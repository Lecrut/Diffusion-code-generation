DIVISOR_4 = 4
DIVISOR_100 = 100
DIVISOR_400 = 400

def is_divisible(val, divisor):
    return val % divisor == 0

def is_leap_year(year):
    check_century = is_divisible(year, DIVISOR_100)
    check_four_hundred = is_divisible(year, DIVISOR_400)
    if check_century:
        return check_four_hundred
    check_four = is_divisible(year, DIVISOR_4)
    return check_four

if __name__ == '__main__':
    years = [2000, 1900, 2024]
    for y in years:
        print(is_leap_year(y))