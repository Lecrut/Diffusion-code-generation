from datetime import datetime

def days_difference():
    date1 = datetime(2023, 9, 1)
    date2 = datetime(2023, 10, 15)
    return (date2 - date1).days

if __name__ == '__main__':
    print(f"Days between 2023-09-01 and 2023-10-15: {days_difference()}")