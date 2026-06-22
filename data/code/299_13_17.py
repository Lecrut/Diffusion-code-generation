from datetime import date

def is_weekend(day):
    return day.weekday() >= 5

if __name__ == '__main__':
    sample_dates = {
        '2023-10-21': date(2023, 10, 21),
        '2023-10-22': date(2023, 10, 22),
        '2023-10-23': date(2023, 10, 23)
    }
    
    for label, day in sample_dates.items():
        print(f'{label}: {is_weekend(day)}')