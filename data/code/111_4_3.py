import datetime
def manipulate_date():
    start_date_str = "2023-10-26"
    days_to_add = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    new_day = start_date.day + days_to_add
    try:
        new_date = start_date.replace(day=new_day)
        print(new_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Error: The resulting day is out of range for the month.")
if __name__ == '__main__':
    manipulate_date()