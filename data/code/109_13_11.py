import datetime

def days_left_in_month(start_date):
    months = {
        1: 31, 2: 28, 3: 31, 4: 30, 
        5: 31, 6: 30, 7: 31, 8: 31, 
        9: 30, 10: 31, 11: 30, 12: 31
    }
    if start_date.month == 2 and (start_date.year % 4 == 0 and start_date.year % 100 != 0 or start_date.year % 400 == 0):
        months[2] = 29
    return months[start_date.month] - start_date.day

if __name__ == '__main__':
    sample_date = datetime.date(2023, 10, 15)
    print(days_left_in_month(sample_date))