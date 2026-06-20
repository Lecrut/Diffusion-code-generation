import datetime

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

def calculate_year_difference(date1, date2):
    if not isinstance(date1, datetime.date) or not isinstance(date2, datetime.date):
        raise ValueError("Both inputs must be of type datetime.date")
    return abs((date1 - date2).days // 365)

if __name__ == '__main__':
    date1 = parse_date("2023-04-15")
    date2 = parse_date("1990-07-28")
    result = calculate_year_difference(date1, date2)
    print(result)