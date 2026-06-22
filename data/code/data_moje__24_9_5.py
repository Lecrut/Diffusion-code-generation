DIVISIBLE_BY_4 = 4
DIVISIBLE_BY_100 = 100
DIVISIBLE_BY_400 = 400

def is_leap_year(year):
    mod_4 = year % DIVISIBLE_BY_4
    mod_100 = year % DIVISIBLE_BY_100
    mod_400 = year % DIVISIBLE_BY_400
    if mod_400 == 0:
        return True
    if mod_100 == 0:
        return False
    return mod_4 == 0

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2100))
    print(is_leap_year(2400))