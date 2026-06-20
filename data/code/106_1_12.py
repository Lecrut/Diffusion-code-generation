import datetime

def calculate_year_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        
        year_diff = abs((date1.year - date2.year))
        if (date1.month < date2.month) or (date1.month == date2.month and date1.day < date2.day):
            year_diff -= 1
        return year_diff
    except ValueError as e:
        print(f"Invalid date format. Please use YYYY-MM-DD: {e}")
        raise

if __name__ == '__main__':
    date1 = "2023-04-15"
    date2 = "1998-06-20"
    result = calculate_year_difference(date1, date2)
    print(result)