from datetime import datetime
def calculate_difference(date1, date2):
    return date2 - date1
if __name__ == '__main__':
    d1 = datetime(2023, 1, 1)
    d2 = datetime(2023, 1, 10)
    difference = calculate_difference(d1, d2)
    print(difference)