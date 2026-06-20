from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%m/%d/%Y').date()
    except ValueError:
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")

def calculate_difference(date1_str, date2_str):
    date1 = parse_date(date1_str)
    date2 = parse_date(date2_str)
    return abs((date2 - date1).days)

if __name__ == '__main__':
    result = calculate_difference('01/01/2023', '01/10/2023')
    print(result)