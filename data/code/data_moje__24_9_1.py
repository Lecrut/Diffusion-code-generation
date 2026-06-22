DIVISORS = {4: 0, 100: 0, 400: 0}

def is_leap_year(year):
    remainder = year % 400
    if remainder == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2004))