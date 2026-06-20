import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def calculate_time_difference(date_str1, date_str2):
    parsed_date1 = parse_date(date_str1)
    parsed_date2 = parse_date(date_str2)
    difference = abs(parsed_date1 - parsed_date2)
    return difference

if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2022-11-20"
    date_c = "2023/01/10"
    
    print(f"Difference between {date_a} and {date_b}: {calculate_time_difference(date_a, date_b)}")
    print(f"Difference between {date_a} and {date_c}: {calculate_time_difference(date_a, date_c)} days")