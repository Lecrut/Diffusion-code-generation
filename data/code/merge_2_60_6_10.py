import sys
def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if __name__ == '__main__':
    start_year = 2000
    end_year = 2036
    leap_years_list = []
    for current_year in range(start_year, end_year + 1):
        if is_leap_year(current_year):
            leap_years_list.append(str(current_year))
    print(", ".join(leap_years_list))