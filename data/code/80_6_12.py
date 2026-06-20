from datetime import date

def compare_dates(date_str: str, date_obj: date) -> date:
    date_str_obj = date.fromisoformat(date_str)
    return min(date_str_obj, date_obj)

if __name__ == '__main__':
    sample_date_str = '2023-10-05'
    sample_date_obj = date(2023, 9, 15)
    earlier_date = compare_dates(sample_date_str, sample_date_obj)
    print(earlier_date)