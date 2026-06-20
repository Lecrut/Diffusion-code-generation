from datetime import datetime

def date_difference_days(date1, date2):
    return abs((date1 - date2).days)

if __name__ == '__main__':
    sample_dates = {
        '2023-01-01': datetime(2023, 1, 1),
        '2023-01-10': datetime(2023, 1, 10),
        '2024-05-15': datetime(2024, 5, 15),
        '2024-04-01': datetime(2024, 4, 1),
        '2022-12-31': datetime(2022, 12, 31),
        '2023-01-02': datetime(2023, 1, 2)
    }

    for date_str, date_obj in sample_dates.items():
        if date_str == '2023-01-01':
            result = date_difference_days(date_obj, sample_dates['2023-01-10'])
            print(f"Difference between {date_str} and 2023-01-10: {result}")
        elif date_str == '2024-05-15':
            result = date_difference_days(date_obj, sample_dates['2024-04-01'])
            print(f"Difference between {date_str} and 2024-04-01: {result}")
        elif date_str == '2022-12-31':
            result = date_difference_days(date_obj, sample_dates['2023-01-02'])
            print(f"Difference between {date_str} and 2023-01-02: {result}")