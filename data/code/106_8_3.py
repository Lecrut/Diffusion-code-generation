def calculate_year_difference(date_str1, date_str2):
    year1 = int(date_str1)
    year2 = int(date_str2)
    return year2 - year1
if __name__ == '__main__':
    date1 = "2020"
    date2 = "1995"
    difference = calculate_year_difference(date1, date2)
    print(difference)