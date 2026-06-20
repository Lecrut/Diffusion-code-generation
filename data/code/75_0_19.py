import datetime

def parse_date(date_string):
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    raise ValueError("Date string is not in a recognized format")

def calculate_date_difference(date_string1, date_string2):
    date1 = parse_date(date_string1)
    date2 = parse_date(date_string2)
    return abs((date1 - date2).days)

if __name__ == '__main__':
    print(calculate_date_difference("2023-04-10", "10/04/2023"))