from datetime import date

def compare_dates(date_str, date_obj):
    date_str = date.fromisoformat(date_str)
    return min(date_str, date_obj)

if __name__ == '__main__':
    result = compare_dates('2023-10-05', date(2023, 10, 10))
    print(result)