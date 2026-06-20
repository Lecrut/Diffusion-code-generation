from datetime import date

def get_weekday_name(year, month, day):
    return date(year, month, day).strftime("%A")

if __name__ == '__main__':
    sample_date_1 = (2023, 10, 26)
    print(get_weekday_name(*sample_date_1))
    sample_date_2 = (2024, 1, 1)
    print(get_weekday_name(*sample_date_2))
    sample_date_3 = (2025, 12, 31)
    print(get_weekday_name(*sample_date_3))