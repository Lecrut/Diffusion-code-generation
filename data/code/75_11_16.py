from datetime import datetime

def date_difference(date_str1, date_str2):
    format_str = "%Y-%m-%d"
    a = datetime.strptime(date_str1, format_str)
    b = datetime.strptime(date_str2, format_str)
    delta = abs(b - a)
    days = delta.days
    months = delta.days // 30
    remaining_days = delta.days % 30
    return f"{months} months, {remaining_days} days"

if __name__ == '__main__':
    print(date_difference("2023-01-01", "2024-02-15"))