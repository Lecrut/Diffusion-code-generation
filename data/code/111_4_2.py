import datetime
def manipulate_date():
    start_date_str = "2023-10-25"
    days_to_add = 10
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    new_day = start_date.day + days_to_add
    if new_day > 31:
        month = start_date.month
        year = start_date.year
        while True:
            if month < 12:
                new_day -= (31 if month == 12 else 30)
                if new_day <= 0:
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                    new_day = new_day + 31
                else:
                    break
            else:
                month = 1
                year += 1
                new_day = new_day - 31
                break
    end_date = datetime.date(start_date.year, start_date.month, new_day)
    print(end_date.strftime("%Y-%m-%d"))
if __name__ == '__main__':
    manipulate_date()