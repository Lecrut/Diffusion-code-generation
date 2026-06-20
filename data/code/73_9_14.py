import datetime

def calculate_time_difference(date1, date2):
    if not isinstance(date1, datetime.datetime) or not isinstance(date2, datetime.datetime):
        raise ValueError("Both inputs must be datetime objects.")
    
    return abs(date1 - date2)

if __name__ == '__main__':
    date_a = datetime.datetime(2023, 1, 15)
    date_b = datetime.datetime(2023, 2, 20)
    print(f"Difference between {date_a} and {date_b}: {calculate_time_difference(date_a, date_b)}")

    invalid_date_c = "2023-03-10"
    try:
        date_c = datetime.datetime.strptime(invalid_date_c, '%Y-%m-%d')
        print(f"Difference between {date_a} and {date_c}: {calculate_time_difference(date_a, date_c)}")
    except ValueError as e:
        print(e)