import calendar

def reformat_date(date_str):
    year, month, day = map(int, date_str.split('-'))
    month_name = calendar.month_name[month]
    return f"{month_name} {day}, {year}"

if __name__ == '__main__':
    sample_date = '2023-10-5'
    print(reformat_date(sample_date))