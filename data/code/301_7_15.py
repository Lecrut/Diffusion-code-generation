from datetime import datetime

WEEKDAY_NAMES = [
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

def get_weekday(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%d')
    weekday_index = date_object.weekday()
    return WEEKDAY_NAMES[weekday_index]

if __name__ == '__main__':
    sample_date1 = '2023-10-27'
    result1 = get_weekday(sample_date1)
    print(f"{sample_date1} -> {result1}")
    
    sample_date2 = '2024-01-01'
    result2 = get_weekday(sample_date2)
    print(f"{sample_date2} -> {result2}")
    
    sample_date3 = '2023-12-31'
    result3 = get_weekday(sample_date3)
    print(f"{sample_date3} -> {result3}")