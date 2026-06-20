from datetime import datetime

def calculate_year_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    return abs((date2 - date1).days // 365)

if __name__ == '__main__':
    print(calculate_year_difference("2023-10-01", "1998-05-15"))
    print(calculate_year_difference("2000-01-01", "2024-03-20"))
    print(calculate_year_difference("1850-12-31", "1900-01-01"))