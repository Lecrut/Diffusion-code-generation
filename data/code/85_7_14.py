from datetime import datetime

WEEKS_PER_DAY = 7

def calculate_week_difference(date_str1, date_str2):
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    difference = abs((date2 - date1).days)
    weeks = difference / WEEKS_PER_DAY
    return weeks

if __name__ == '__main__':
    result = calculate_week_difference("2023-01-01", "2023-01-29")
    print(f"The difference is approximately {result:.2f} weeks.")