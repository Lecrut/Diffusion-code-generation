from datetime import date

def is_weekend(dt: date) -> bool:
    day_of_week = dt.weekday()
    return day_of_week >= 5

if __name__ == '__main__':
    date1 = date(2023, 10, 9)
    date2 = date(2023, 10, 10)
    date3 = date(2023, 10, 11)
    
    results = {
        '2023-10-09': is_weekend(date1),
        '2023-10-10': is_weekend(date2),
        '2023-10-11': is_weekend(date3)
    }
    
    print(results)