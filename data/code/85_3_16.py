def weeks_between_julian_dates(date1, date2):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))
    
    def days_in_year(year):
        return 365 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    
    def days_since_julian_start(year, month, day):
        days = sum(days_in_month[:month-1])
        if month > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days += 1
        return days + day
    
    start_days = days_since_julian_start(year1, month1, day1)
    end_days = days_since_julian_start(year2, month2, day2)
    
    total_days = abs(end_days - start_days)
    weeks = total_days // 7
    return weeks

if __name__ == '__main__':
    print(weeks_between_julian_dates('2023-01-01', '2024-01-01'))