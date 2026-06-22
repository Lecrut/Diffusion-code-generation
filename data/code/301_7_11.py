from datetime import datetime

def get_day_of_week(date_string):
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.strftime('%A')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date1 = '2023-10-27'
    day_of_week1 = get_day_of_week(sample_date1)
    print(f"{sample_date1} -> {day_of_week1}")
    sample_date2 = '2024-01-01'
    day_of_week2 = get_day_of_week(sample_date2)
    print(f"{sample_date2} -> {day_of_week2}")