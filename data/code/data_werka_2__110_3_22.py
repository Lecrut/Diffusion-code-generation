from datetime import date

def sort_dates(dates):
    if not dates:
        return []
    return sorted([d for d in dates])

if __name__ == '__main__':
    sample_dates = [date(2023, 6, 1), date(2021, 1, 1), date(2022, 12, 31)]
    print(sort_dates(sample_dates))