def _validate_year(year):
    if not isinstance(year, int):
        return False
    if year <= 0:
        return False
    return True

def check_leap(year):
    if not _validate_year(year):
        return False
    divisible_by_4 = (year % 4 == 0)
    divisible_by_100 = (year % 100 == 0)
    divisible_by_400 = (year % 400 == 0)
    if divisible_by_400:
        return True
    if divisible_by_100:
        return False
    return divisible_by_4

if __name__ == '__main__':
    sample_years = [2024, 1900, 2000, 1600, 2023, 2100]
    for y in sample_years:
        result = check_leap(y)
        print(f"{y}: {result}")