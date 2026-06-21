from datetime import date

def sort_dates(dates):
    if not all(isinstance(d, date) for d in dates):
        raise ValueError("All items must be date objects")
    return sorted([d for d in dates])

if __name__ == '__main__':
    sample_dates = [date(2024, 2, 1), date(2022, 11, 5), date(2023, 7, 20)]
    print(sort_dates(sample_dates))