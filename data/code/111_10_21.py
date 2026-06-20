from datetime import datetime

def days_difference():
    try:
        date1 = datetime(2023, 9, 1)
        date2 = datetime(2023, 10, 15)
        delta = abs((date2 - date1).days)
        return delta
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    result = days_difference()
    if result is not None:
        print(f"Days difference between dates: {result}")