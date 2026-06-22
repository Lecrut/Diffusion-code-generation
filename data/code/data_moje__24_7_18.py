DIVISOR_ONE = 4
DIVISOR_TWO = 100
DIVISOR_THREE = 400

def is_leap_year(year):
    return (year % DIVISOR_ONE == 0) and ((year % DIVISOR_TWO != 0) or (year % DIVISOR_THREE == 0))

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(1600))
    print(is_leap_year(1700))
    print(is_leap_year(2400))
    print(is_leap_year(2100))