from datetime import date

def string_to_date(date_str):
    parts = date_str.split('-')
    if len(parts) != 3:
        raise ValueError("Date strings must be in 'YYYY-MM-DD' format.")
    year, month, day = map(int, parts)
    return date(year, month, day)

def compare_dates(date_str1, date_obj2):
    date_obj1 = string_to_date(date_str1)
    if date_obj1 < date_obj2:
        return date_obj1
    else:
        return date_obj2

if __name__ == '__main__':
    sample_date_str = "2023-04-15"
    sample_date_obj = date(2023, 4, 16)
    earlier_date = compare_dates(sample_date_str, sample_date_obj)
    print(earlier_date)