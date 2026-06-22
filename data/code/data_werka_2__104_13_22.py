import datetime

WEEK_START_DAY = 0
WEEK_END_DAY = 6

def is_same_week(date_first: datetime.date, date_second: datetime.date) -> bool:
    iso_first = date_first.isocalendar()
    iso_second = date_second.isocalendar()
    return iso_first[0] == iso_second[0] and iso_first[1] == iso_second[1]

if __name__ == '__main__':
    start_of_year = datetime.date(2024, 1, 1)
    end_of_first_week = datetime.date(2024, 1, 7)
    start_of_second_week = datetime.date(2024, 1, 8)
    print(is_same_week(start_of_year, end_of_first_week))
    print(is_same_week(start_of_year, start_of_second_week))