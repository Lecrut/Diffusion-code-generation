from datetime import date

def identical_date_pairs(dates):
    for i in range(len(dates) - 1):
        if dates[i] == dates[i + 1]:
            yield True

if __name__ == '__main__':
    sample_dates = [
        date(2023, 10, 27),
        date(2023, 10, 28),
        date(2023, 10, 29),
        date(2023, 10, 28)
    ]
    
    for pair in identical_date_pairs(sample_dates):
        print(pair)