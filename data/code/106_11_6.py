def calculate_year_difference(date_str1, date_str2):
    year1 = int(date_str1.split('-')[0])
    year2 = int(date_str2.split('-')[0])
    return abs(year1 - year2)

if __name__ == '__main__':
    date1 = '2023-04-15'
    date2 = '1998-11-22'
    difference = calculate_year_difference(date1, date2)
    print(difference)