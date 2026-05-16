import datetime
def manipulate_date():
    start_date_str = "2023-10-26"
    days_to_add_str = "10"
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d").date()
    days_to_add = int(days_to_add_str)
    new_day = start_date.day + days_to_add
    new_year = start_date.year
    new_month = start_date.month
    if new_day > 31:
        new_month += (new_day - 31) // 30
        new_day = new_day % 30
        if new_day == 0:
            new_day = 30
        if new_month > 12:
            new_month -= 12
            new_day += 30
            if new_day > 31:
                new_day = 1
                new_month += 1
    else:
        new_year_temp = new_year
        new_month_temp = new_month
        if new_day > 28:
            if new_month == 2:
                new_month_temp = 3
                new_day = new_day - 28
            else:
                new_day = new_day - 31
                new_month_temp = new_month + 1
        if new_day > 31:
            new_month_temp = new_month + (new_day - 31) // 30
            new_day = new_day % 30
            if new_day == 0:
                new_day = 30
            if new_month_temp > 12:
                new_month_temp -= 12
                new_day += 30
                if new_day > 31:
                    new_day = 1
                    new_month_temp += 1
        if new_month_temp > 12:
            new_month_temp -= 12
            new_year_temp += 1
        new_year = new_year_temp
        new_month = new_month_temp
    result_date = datetime.date(new_year, new_month, new_day)
    print(result_date.strftime("%Y-%m-%d"))
if __name__ == '__main__':
    manipulate_date()