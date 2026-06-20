import datetime

def validate_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

def order_dates(date1_str, date2_str):
    date1 = validate_date(date1_str)
    date2 = validate_date(date2_str)
    return (date1, date2) if date1 < date2 else (date2, date1)

if __name__ == '__main__':
    date_a = "2023-10-26"
    date_b = "2023-10-20"
    print(order_dates(date_a, date_b))