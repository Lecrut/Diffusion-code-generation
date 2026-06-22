from datetime import datetime

def convert_to_day_name(date_string):
    try:
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        return date_object.strftime('%A')
    except ValueError:
        return "Invalid date format"

if __name__ == '__main__':
    sample_date1 = '2023-10-27'
    result1 = convert_to_day_name(sample_date1)
    print(f"{sample_date1} -> {result1}")
    sample_date2 = '2024-01-01'
    result2 = convert_to_day_name(sample_date2)
    print(f"{sample_date2} -> {result2}")