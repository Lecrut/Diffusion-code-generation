def compute_year_difference(date1: str, date2: str) -> int:
    year1 = int(date1[:4])
    year2 = int(date2[:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    result = compute_year_difference('2023-10-01', '2020-05-15')
    print(result)