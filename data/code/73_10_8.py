from datetime import datetime

def days_between_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    dt1 = datetime.strptime(date_str1, date_format)
    dt2 = datetime.strptime(date_str2, date_format)
    return abs((dt2 - dt1).days)

if __name__ == '__main__':
    sample_dates = {
        "date1": "2023-01-01",
        "date2": "2023-01-05",
        "date3": "2023-02-15"
    }
    
    for date_key in sample_dates:
        print(f"Days between {sample_dates[date_key]} and {sample_dates['date1']}: {days_between_dates(sample_dates[date_key], sample_dates['date1'])}")