from datetime import datetime
def date_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    diff = date2 - date1
    years = diff.days // 365
    months = diff.days // 30
    remaining_days = diff.days % 30
    if months >= 12:
        years += months // 12
        months %= 12
    return f"{diff.days} days"
if __name__ == '__main__':
    date1 = "2023-01-15"
    date2 = "2024-03-20"
    result = date_difference(date1, date2)
    print(f"Difference between {date1} and {date2}: {result}")