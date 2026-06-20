from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    year_diff = abs((date2.year - date1.year) + (date2.month > date1.month or (date2.month == date1.month and date2.day >= date1.day)))
    return year_diff

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    print(calculate_year_difference(sample_date1, sample_date2))