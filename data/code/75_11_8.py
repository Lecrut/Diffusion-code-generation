from datetime import datetime

def date_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    
    delta = abs((date2 - date1).days)
    years = delta // 365
    months = (delta % 365) // 30
    days = (delta % 365) % 30
    
    return f"{years} years, {months} months, and {days} days"

if __name__ == '__main__':
    print(date_difference("2020-01-01", "2023-04-15"))