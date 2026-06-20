import datetime

def calculate_date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date_str1, date_format).date()
    date2 = datetime.datetime.strptime(date_str2, date_format).date()
    
    if date1 > date2:
        start_date = date2
        end_date = date1
    else:
        start_date = date1
        end_date = date2
    
    time_difference = end_date - start_date
    return time_difference.days

if __name__ == '__main__':
    date_str1 = "2023-01-15"
    date_str2 = "2021-11-20"
    difference = calculate_date_difference(date_str1, date_str2)
    print(f"Date Difference: {difference} days")