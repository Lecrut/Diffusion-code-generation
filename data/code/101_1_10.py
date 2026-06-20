import calendar

def get_weekday_name(year, month, day):
    date_obj = calendar.date(year, month, day)
    return date_obj.strftime("%A")

if __name__ == '__main__':
    sample_year_1, sample_month_1, sample_day_1 = 2023, 10, 26
    sample_year_2, sample_month_2, sample_day_2 = 2024, 1, 1
    sample_year_3, sample_month_3, sample_day_3 = 2025, 12, 31
    
    print(get_weekday_name(sample_year_1, sample_month_1, sample_day_1))
    print(get_weekday_name(sample_year_2, sample_month_2, sample_day_2))
    print(get_weekday_name(sample_year_3, sample_month_3, sample_day_3))