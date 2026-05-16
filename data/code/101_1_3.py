from datetime import date
def determine_weekday(date_obj):
    return date_obj.strftime("%A")
if __name__ == '__main__':
    date1 = date(2023, 10, 26)
    date2 = date(2024, 1, 1)
    date3 = date(2025, 12, 31)
    print(determine_weekday(date1))
    print(determine_weekday(date2))
    print(determine_weekday(date3))