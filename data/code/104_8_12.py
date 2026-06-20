from dateutil.relativedelta import relativedelta

def is_within_one_week(date1_str, date2_str):
    try:
        from dateutil.parser import parse
        date1 = parse(date1_str).date()
        date2 = parse(date2_str).date()
        
        return abs((date1 - date2).days) <= 7
    except ValueError as e:
        print(f"Error parsing dates: {e}")
        return False

if __name__ == '__main__':
    sample_date_a = '2023-10-26'
    sample_date_b = '2023-11-04'
    result = is_within_one_week(sample_date_a, sample_date_b)
    print(result)

    sample_date_c = '2024-01-01'
    sample_date_d = '2023-12-31'
    result2 = is_within_one_week(sample_date_c, sample_date_d)
    print(result2)