from datetime import datetime
def determine_weekday(date_obj):
    return date_obj.strftime("%A")
if __name__ == '__main__':
    date1 = datetime(2023, 10, 26)
    date2 = datetime(2024, 1, 1)
    date3 = datetime(2023, 12, 25)
    print(determine_weekday(date1))
    print(determine_weekday(date2))
    print(determine_weekday(date3))