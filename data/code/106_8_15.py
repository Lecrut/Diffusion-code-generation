from datetime import datetime

YEAR_CONVERSION = 365

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    days_diff = abs((date2 - date1).days)
    return days_diff // YEAR_CONVERSION

if __name__ == '__main__':
    sample_date1 = "2000-01-01"
    sample_date2 = "1995-06-30"
    difference = calculate_year_difference(sample_date1, sample_date2)
    print(difference)