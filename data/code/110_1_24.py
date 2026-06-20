from datetime import datetime

def sort_datetimes(dt_list):
    return sorted(dt_list)

if __name__ == '__main__':
    sample_dts = [datetime(2023, 1, 5), datetime(2022, 12, 25), datetime(2023, 1, 1)]
    sorted_dts = sort_datetimes(sample_dts)
    print(sorted_dts)