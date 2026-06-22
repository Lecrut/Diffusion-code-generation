def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2004) == True

if __name__ == '__main__':
    sample_years = [2000, 1900, 2004, 2023]
    results = []
    for y in sample_years:
        results.append({"year": y, "is_leap": is_leap_year(y)})
    print(results)