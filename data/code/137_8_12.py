def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

if __name__ == '__main__':
    year1 = 2000
    year2 = 1900
    year3 = 2020
    year4 = 2021
    
    result1 = is_leap_year(year1)
    result2 = is_leap_year(year2)
    result3 = is_leap_year(year3)
    result4 = is_leap_year(year4)
    
    print(f"Year {year1} is leap year: {result1}")
    print(f"Year {year2} is leap year: {result2}")
    print(f"Year {year3} is leap year: {result3}")
    print(f"Year {year4} is leap year: {result4}")