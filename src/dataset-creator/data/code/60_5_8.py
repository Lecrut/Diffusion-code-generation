def is_leap_year(year):
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023]
    for current_year in sample_years:
        result_status = is_leap_year(current_year)
        print(f"Year {current_year}: {'Leap Year' if result_status else 'Not a Leap Year'}")