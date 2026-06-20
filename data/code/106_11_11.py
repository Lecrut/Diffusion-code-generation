def calculate_year_difference(date_str1, date_str2):
    year1 = int(date_str1.split('-')[0])
    year2 = int(date_str2.split('-')[0])
    return abs(year1 - year2)

if __name__ == '__main__':
    sample_date1 = '2023-04-15'
    sample_date2 = '1998-11-25'
    difference = calculate_year_difference(sample_date1, sample_date2)
    print(difference)