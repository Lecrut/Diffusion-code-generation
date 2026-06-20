from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    year1 = int(date_str1[:4])
    year2 = int(date_str2[:4])
    return abs(year1 - year2)

if __name__ == '__main__':
    date1 = "2000-12-31"
    date2 = "1995-01-01"
    difference = calculate_year_difference(date1, date2)
    print(difference)