import calendar

def months_between_dates(date_str1, date_str2):
    year1, month1, day1 = map(int, date_str1.split('-'))
    year2, month2, day2 = map(int, date_str2.split('-'))
    
    start_date = calendar.datetime(year1, month1, day1)
    end_date = calendar.datetime(year2, month2, day2)
    
    difference_years = end_date.year - start_date.year
    difference_months = end_date.month - start_date.month
    
    total_difference = (difference_years * 12) + difference_months
    
    return abs(total_difference)

if __name__ == '__main__':
    date_str1 = '2019-05-10'
    date_str2 = '2024-03-20'
    result = months_between_dates(date_str1, date_str2)
    print(result)