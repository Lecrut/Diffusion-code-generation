import calendar

def months_between_dates(date_str1, date_str2):
    try:
        year1, month1, day1 = map(int, date_str1.split('-'))
        year2, month2, day2 = map(int, date_str2.split('-'))
        
        if not (1 <= month1 <= 12 and 1 <= month2 <= 12):
            raise ValueError("Invalid month value. Month should be between 1 and 12.")
        
        start_date = calendar.datetime(year1, month1, day1)
        end_date = calendar.datetime(year2, month2, day2)
        
        if start_date > end_date:
            raise ValueError("The first date must be before the second date.")
        
        difference = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
        return difference
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    date_str1 = '2020-01-01'
    date_str2 = '2023-04-15'
    result = months_between_dates(date_str1, date_str2)
    print(result)