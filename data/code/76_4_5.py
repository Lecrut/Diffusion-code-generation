from datetime import datetime

def days_difference(date_str1, date_str2):
    try:
        date_format = "%m/%d/%Y"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return abs((date2 - date1).days)
    except ValueError:
        return "Invalid date format. Please use MM/DD/YYYY."

if __name__ == '__main__':
    print(days_difference("01/01/2020", "12/31/2020"))
    print(days_difference("02/29/2020", "02/28/2020"))
    print(days_difference("04/31/2020", "05/01/2020"))
    print(days_difference("13/01/2020", "01/13/2020"))