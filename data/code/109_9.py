import datetime
if __name__ == '__main__':
    today = datetime.date.today()
    target_month = 3                                                                                                                   
    current_year = today.year
    current_month = today.month
    if current_month == 12:
        next_month = 1
        next_year = current_year + 1
    else:
        next_month = current_month + 1
        next_year = current_year
    end_of_next_month = datetime.date(next_year, next_month, 1)
    time_remaining = (end_of_next_month - today).days
    print(time_remaining)