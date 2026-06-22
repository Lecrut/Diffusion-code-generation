from datetime import date

def calculate_absolute_year_difference(first_date: date, second_date: date) -> int:
    year1 = first_date.year
    year2 = second_date.year
    month1 = first_date.month
    day1 = first_date.day
    month2 = second_date.month
    day2 = second_date.day
    if year1 == year2:
        return 0
    base_diff = abs(year1 - year2) - 1
    date1_later_in_year = (month1, day1) > (month2, day2)
    date2_later_in_year = (month2, day2) > (month1, day1)
    if date1_later_in_year and date2_later_in_year:
        return base_diff + 1
    if date1_later_in_year or date2_later_in_year:
        return base_diff + 1
    return base_diff

if __name__ == '__main__':
    start = date(2018, 12, 31)
    end = date(2021, 1, 1)
    diff_years = calculate_absolute_year_difference(start, end)
    print(diff_years)