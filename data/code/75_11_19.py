from datetime import datetime

def date_diff(date_str1, date_str2):
    format = "%Y-%m-%d"
    a = datetime.strptime(date_str1, format)
    b = datetime.strptime(date_str2, format)
    delta = abs(b - a)
    days = delta.days
    months = delta.days // 30
    return f"{months} months, {days % 30} days"

if __name__ == '__main__':
    print(date_diff("2022-01-01", "2022-02-01"))