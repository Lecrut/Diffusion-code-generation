from datetime import datetime
def calculate_days_between(date1_str, date2_str):
    date1 = datetime.strptime(date1_str, "%Y-%m-%d")
    date2 = datetime.strptime(date2_str, "%Y-%m-%d")
    time_difference = abs(date2 - date1)
    return time_difference.days
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-03-20"
    days = calculate_days_between(date_a, date_b)
    print(days)