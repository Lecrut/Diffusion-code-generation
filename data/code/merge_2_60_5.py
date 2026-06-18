def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
if __name__ == '__main__':
    sample_years = [2000, 1900, 2024, 2023, 2500]
    print("Leap Year Checker Results")
    print("-" * 30)
    for current_year in sample_years:
        result = is_leap_year(current_year)
        output_string = f"{current_year}: {'LEAP YEAR' if result else 'COMMON YEAR'}"
        print(output_string)