from datetime import datetime

def calculate_age_difference(date_str1, date_str2):
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        age_diff = abs((date2 - date1).days) // 365
        return age_diff
    except ValueError as e:
        print(f"Error: Invalid date format. Please use YYYY-MM-DD.", file=sys.stderr)
        raise

if __name__ == '__main__':
    sample_date1 = "1990-05-15"
    sample_date2 = "2023-04-10"
    try:
        difference = calculate_age_difference(sample_date1, sample_date2)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")