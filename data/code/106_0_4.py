from datetime import datetime

def calculate_age_difference(date_str1, date_str2):
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        if date1 > date2:
            date1, date2 = date2, date1
        age_difference = abs((date2 - date1).days) // 365
        return age_difference
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    age_diff = calculate_age_difference(sample_date1, sample_date2)
    if age_diff is not None:
        print(age_diff)