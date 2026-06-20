def month_difference(timestamp1, timestamp2):
    def days_in_month(year, month):
        if month == 2:
            return 29 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    year1, month1 = timestamp1 // 31536000 + 1970, timestamp1 % 31536000 // 2628000
    day1 = timestamp1 % 2628000 // 86400
    year2, month2 = timestamp2 // 31536000 + 1970, timestamp2 % 31536000 // 2628000

    if year1 == year2:
        return abs(month2 - month1)
    
    month_diff = 0
    for year in range(year1, year2):
        if is_leap_year(year):
            month_diff += (13 - month1) + month2
        else:
            month_diff += (12 - month1) + month2
        month1 = 1
        month2 = 1

    return abs(month_diff)

if __name__ == '__main__':
    print(month_difference(1633075200, 1645196800))