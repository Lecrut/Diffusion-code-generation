from datetime import datetime, timezone

def format_date_string(date_string):
    try:
        naive_dt = datetime.strptime(date_string, '%m/%d/%y')
        utc_dt = naive_dt.replace(tzinfo=timezone.utc)
        offset = utc_dt.utcoffset()
        return f"{offset.total_seconds() // 3600 * 100:+04}"
    except ValueError:
        return None

if __name__ == '__main__':
    date_str_valid = "03/15/23"
    result_valid = format_date_string(date_str_valid)
    print(f"Input: {date_str_valid}, Result: {result_valid}")