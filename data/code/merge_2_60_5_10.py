def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
if __name__ == '__main__':
    SAMPLE_YEARS = [2000, 1900, 2024, 2023]
    print("Leap Year Calculation Results:")
    for year in SAMPLE_YEARS:
        leap_status = is_leap_year(year)
        status_text = "LEAP YEAR" if leap_status else "COMMON YEAR"
        print(f"{year}: {status_text}")