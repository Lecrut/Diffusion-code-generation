from datetime import date

def days_difference(date1, date2):
    return (date2 - date1).days

if __name__ == '__main__':
    print(days_difference(date(2023, 1, 1), date(2023, 1, 31)))