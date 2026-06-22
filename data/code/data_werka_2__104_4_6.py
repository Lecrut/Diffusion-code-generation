from datetime import date

def is_same_date(date1, date2):
    year1, month1, day1 = date1
    year2, month2, day2 = date2
    first_date = date(year1, month1, day1)
    second_date = date(year2, month2, day2)
    return first_date == second_date

if __name__ == '__main__':
    sample1 = (2024, 2, 29)
    sample2 = (2024, 3, 1)
    output = is_same_date(sample1, sample2)
    print(output)