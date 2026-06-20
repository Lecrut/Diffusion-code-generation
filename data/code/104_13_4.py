from datetime import datetime

def is_same_week(date_str1: str, date_str2: str) -> bool:
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    date1_str = "2023-11-01"
    date2_str = "2023-11-07"
    result1 = is_same_week(date1_str, date2_str)
    print(f"{date1_str} and {date2_str} are in the same week: {result1}")
    
    date1_str = "2023-11-08"
    date2_str = "2023-11-14"
    result2 = is_same_week(date1_str, date2_str)
    print(f"{date1_str} and {date2_str} are in the same week: {result2}")
    
    date1_str = "2023-11-01"
    date2_str = "2023-11-08"
    result3 = is_same_week(date1_str, date2_str)
    print(f"{date1_str} and {date2_str} are in the same week: {result3}")