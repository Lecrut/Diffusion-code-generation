import datetime

def calculate_days_difference(date_str1: str, date_str2: str) -> int:
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(date_str1, date_format).date()
    date2 = datetime.datetime.strptime(date_str2, date_format).date()
    
    if date1 > date2:
        return (date1 - date2).days
    else:
        return (date2 - date1).days

if __name__ == '__main__':
    date_str1 = "2023-04-15"
    date_str2 = "2021-11-20"
    days_difference = calculate_days_difference(date_str1, date_str2)
    print(f"Days Difference: {days_difference}")