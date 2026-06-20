from datetime import datetime

def calculate_year_difference(year1: int, year2: int) -> int:
    return abs(year1 - year2)

if __name__ == '__main__':
    date_format = "%Y-%m-%d"
    date1_str = "2023-04-01"
    date2_str = "1998-05-15"

    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    year_difference = calculate_year_difference(date1.year, date2.year)
    print(f"Date 1: {date1_str}")
    print(f"Date 2: {date2_str}")
    print(f"The absolute difference in years between the two dates is: {year_difference}")