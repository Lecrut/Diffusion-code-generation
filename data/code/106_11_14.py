YEAR_CONVERSION = 1

def calculate_difference(date_str1, date_str2):
    year1, _, _ = map(int, date_str1.split('-'))
    year2, _, _ = map(int, date_str2.split('-'))
    return abs(year1 - year2)

if __name__ == '__main__':
    date1 = '2023-10-05'
    date2 = '1998-07-15'
    difference = calculate_difference(date1, date2)
    print(difference)