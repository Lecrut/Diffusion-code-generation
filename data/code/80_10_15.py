import datetime

def compare_dates(date_str1, date_str2):
    DATE_FORMAT = '%Y-%m-%d'
    
    try:
        date1 = datetime.datetime.strptime(date_str1, DATE_FORMAT).date()
        date2 = datetime.datetime.strptime(date_str2, DATE_FORMAT).date()
        
        return min(date1, date2)
    except ValueError:
        raise ValueError("One or both date strings are in an invalid format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_input = "2023-10-25"
    date2_input = "2023-10-15"
    result = compare_dates(date1_input, date2_input)
    print(result)