import datetime

def validate_julian_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def calculate_week_difference(julian_date1, julian_date2):
    if not (validate_julian_date(julian_date1) and validate_julian_date(julian_date2)):
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
    
    date1 = datetime.datetime.strptime(julian_date1, '%Y-%m-%d')
    date2 = datetime.datetime.strptime(julian_date2, '%Y-%m-%d')
    difference = abs(date1 - date2)
    weeks = difference.days / 7
    return weeks

if __name__ == '__main__':
    julian_date1 = "2023-01-15"
    julian_date2 = "2023-03-20"
    result = calculate_week_difference(julian_date1, julian_date2)
    print(f"Difference in weeks: {result:.2f}")