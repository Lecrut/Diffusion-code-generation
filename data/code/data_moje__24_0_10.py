def is_leap_year(year):
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("Year must be an integer")
    if year < 1:
        raise ValueError("Year must be a positive integer")
    
    rule_400 = year % 400 == 0
    rule_100 = year % 100 == 0
    rule_4 = year % 4 == 0
    
    return rule_400 or (rule_4 and not rule_100)

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))