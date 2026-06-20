from datetime import datetime

def calculate_week_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    delta = abs((date2 - date1).days) // 7
    return delta

if __name__ == '__main__':
    sample_date1 = "2023-01-01"
    sample_date2 = "2023-02-01"
    print(calculate_week_difference(sample_date1, sample_date2))