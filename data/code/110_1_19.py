from datetime import datetime

def sort_datetime_list(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dates = [datetime(2023, 7, 4), datetime(2022, 12, 25), datetime(2023, 6, 15)]
    sorted_dates = sort_datetime_list(sample_dates)
    print(sorted_dates)