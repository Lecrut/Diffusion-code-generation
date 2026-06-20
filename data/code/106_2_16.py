from datetime import datetime

def calculate_year_difference(date1: datetime, date2: datetime) -> int:
    return abs((date2.year - date1.year))

if __name__ == '__main__':
    date_format = "%Y-%m-%d"
    dates = {
        "start": "2000-05-15",
        "end": "2023-08-20"
    }
    start_date = datetime.strptime(dates["start"], date_format)
    end_date = datetime.strptime(dates["end"], date_format)
    difference = calculate_year_difference(start_date, end_date)
    print(difference)