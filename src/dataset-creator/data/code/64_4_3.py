import datetime as dt
from dateutil.relativedelta import relativedelta                                                                                                                                                                                                                                              
def format_datetime_object(d: dt.datetime) -> str:
    day = d.day
    month_name_map = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 
                      5: 'May', 6: 'June', 7: 'July', 8: 'August', 
                      9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    month_name = month_name_map[d.month]
    am_pm_suffix = 'AM' if d.hour < 12 else ' PM'
    return f"{day} of {month_name}, {d.year}{am_pm_suffix}"
def format_datetime_object_full(d: dt.datetime) -> str:
    month_names = ["January", "February", "March", "April", 
                   "May", "June", "July", "August", 
                   "September", "October", "November", "December"]
    return f"{d.day} {month_names[d.month - 1]}, {d.year}"
if __name__ == '__main__':
    sample_date = dt.datetime(2023, 5, 17)
    print(format_datetime_object(sample_date))