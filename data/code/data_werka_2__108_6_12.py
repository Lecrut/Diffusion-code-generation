import calendar

def extract_days(date_strings):
    days_list = []
    for date_str in date_strings:
        year_part = int(date_str[:4])
        month_part = int(date_str[5:7])
        day_part = int(date_str[8:10])
        is_valid = calendar.monthrange(year_part, month_part)[1] >= day_part
        if not is_valid:
            raise ValueError(f"Invalid date: {date_str}")
        days_list.append(day_part)
    return days_list

if __name__ == '__main__':
    sample_dates = ["2020-01-15", "2021-07-04", "2022-11-23"]
    result_days = extract_days(sample_dates)
    print(result_days)