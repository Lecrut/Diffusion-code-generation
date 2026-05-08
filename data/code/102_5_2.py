import datetime
def is_weekday(date_str):
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        weekday = date_obj.weekday()
        return 0 <= weekday <= 6
    except ValueError:
        return False
if __name__ == '__main__':
    date1 = "2023-10-27"
    date2 = "2024-02-29"
    date3 = "2023-10-28"
    date4 = "2023-02-28"
    date5 = "2023-02-29"
    print(f"Is {date1} a weekday? {is_weekday(date1)}")
    print(f"Is {date2} a weekday? {is_weekday(date2)}")
    print(f"Is {date3} a weekday? {is_weekday(date3)}")
    print(f"Is {date4} a weekday? {is_weekday(date4)}")
    print(f"Is {date5} a weekday? {is_weekday(date5)}")