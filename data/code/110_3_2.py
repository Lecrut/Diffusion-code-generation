from datetime import datetime
if __name__ == '__main__':
    dates = [datetime(2023, 1, 15), datetime(2022, 12, 31), datetime(2023, 5, 20), datetime(2021, 7, 7)]
    dates.sort(reverse=True)
    print(dates)