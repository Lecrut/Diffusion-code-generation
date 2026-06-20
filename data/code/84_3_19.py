import datetime

def parse_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please provide the date in 'YYYY-MM-DD' format.")

def day_of_year(date_str):
    parsed_date = parse_date(date_str)
    year_start = datetime.datetime(parsed_date.year, 1, 1)
    return (parsed_date - year_start).days + 1

if __name__ == '__main__':
    print(day_of_year('2023-10-27'))