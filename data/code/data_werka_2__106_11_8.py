def compute_year_difference(date1_str, date2_str):
    year1 = int(date1_str[:4])
    year2 = int(date2_str[:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    result = compute_year_difference('2023-10-01', '2020-05-15')
    print(result)