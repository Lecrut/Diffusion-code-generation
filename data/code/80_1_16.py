from datetime import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return min(date1, date2)
    except ValueError:
        raise ValueError("Invalid date format provided. Dates must be in 'YYYY-MM-DD' format.")

if __name__ == '__main__':
    sample_date_a = "2023-10-26"
    sample_date_b = "2023-10-25"
    try:
        earlier_date = compare_dates(sample_date_a, sample_date_b)
        print(f"Comparing {sample_date_a} and {sample_date_b}: {earlier_date}")
    except ValueError as e:
        print(e)

    sample_date_c = "2024-01-01"
    sample_date_d = "2023-12-31"
    try:
        earlier_date = compare_dates(sample_date_c, sample_date_d)
        print(f"Comparing {sample_date_c} and {sample_date_d}: {earlier_date}")
    except ValueError as e:
        print(e)