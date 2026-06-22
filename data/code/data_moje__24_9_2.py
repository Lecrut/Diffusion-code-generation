def is_leap_year(year):
    if not isinstance(year, int):
        raise TypeError("Year must be an integer")
    if year <= 0:
        raise ValueError("Year must be positive")
    
    div4 = year % 4 == 0
    div100 = year % 100 == 0
    div400 = year % 400 == 0
    
    if div400:
        return True
    if div100:
        return False
    return div4

if __name__ == '__main__':
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2024))
    print(is_leap_year(2023))
    print(is_leap_year(2400))
    print(is_leap_year(1700))