from datetime import datetime

def compare_dates(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    return datetime.strptime(date_str1, date_format) < datetime.strptime(date_str2, date_format)

if __name__ == '__main__':
    print(compare_dates("2023-04-01", "2023-04-02"))