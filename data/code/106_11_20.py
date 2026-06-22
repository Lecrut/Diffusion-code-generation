import datetime

MIN_YEAR = 1
MAX_YEAR = 9999
YEAR_OFFSET = 1

def calculate_year_difference(date_string_1: str, date_string_2: str) -> int:
    first_date = datetime.datetime.strptime(date_string_1, "%Y-%m-%d")
    second_date = datetime.datetime.strptime(date_string_2, "%Y-%m-%d")
    year_diff = first_date.year - second_date.year
    return year_diff if year_diff >= MIN_YEAR else -year_diff

if __name__ == '__main__':
    start_date = "2010-05-20"
    end_date = "2020-08-15"
    diff = calculate_year_difference(start_date, end_date)
    print(diff)