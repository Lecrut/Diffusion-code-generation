from datetime import datetime

def calculate_week_difference(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    difference = abs((date2 - date1).days)
    weeks = difference / 7
    return weeks

if __name__ == '__main__':
    result = calculate_week_difference("2023-01-01", "2023-01-22")
    print(f"The difference in weeks is: {result:.2f}")