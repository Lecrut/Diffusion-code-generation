DIVISORS = [400, 100, 4]

def is_leap_year(year):
    return (year % DIVISORS[0] == 0) or ((year % DIVISORS[1] != 0) and (year % DIVISORS[2] == 0))

if __name__ == '__main__':
    print(is_leap_year(1600))
    print(is_leap_year(1700))
    print(is_leap_year(2004))
    print(is_leap_year(2001))
    print(is_leap_year(2000))
    print(is_leap_year(1900))