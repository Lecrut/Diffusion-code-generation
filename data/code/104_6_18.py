from datetime import datetime

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError as e:
        print(f"Invalid date format: {date_str}. Please use YYYY-MM-DD.")
        raise e

def compare_dates(date_str1, date_str2):
    date1 = parse_date(date_str1)
    date2 = parse_date(date_str2)
    
    if date1 < date2:
        return "Date 1 is earlier"
    elif date1 > date2:
        return "Date 1 is later"
    else:
        return "Dates are the same"

if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-03-20"
    result = compare_dates(date_a, date_b)
    print(result)

    date_c = "2024-05-20"
    date_d = "2024-03-10"
    result = compare_dates(date_c, date_d)
    print(result)