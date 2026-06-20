from datetime import datetime, timedelta

def dates_in_same_week(date1_str, date2_str):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    start_of_week1 = date1 - timedelta(days=date1.weekday())
    end_of_week1 = start_of_week1 + timedelta(days=6)
    
    start_of_week2 = date2 - timedelta(days=date2.weekday())
    end_of_week2 = start_of_week2 + timedelta(days=6)
    
    return start_of_week1 <= date2 <= end_of_week1 or start_of_week2 <= date1 <= end_of_week2

if __name__ == '__main__':
    print(dates_in_same_week("2023-10-01", "2023-10-07"))
    print(dates_in_same_week("2023-10-01", "2023-10-08"))