from datetime import date

def sort_dates(dates):
    return sorted([d for d in dates])

if __name__ == '__main__':
    dates_list = [date(2022, 8, 14), date(2019, 3, 22), date(2024, 1, 1)]
    ordered_dates = sort_dates(dates_list)
    print(ordered_dates)