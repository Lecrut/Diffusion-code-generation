from datetime import datetime

def is_date_earlier(date_str1: str, date_str2: str) -> bool:
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        return date1 < date2
    except ValueError:
        raise ValueError("One or both date strings are not in the expected YYYY-MM-DD format.")

if __name__ == '__main__':
    sample_date1 = "2023-09-05"
    sample_date2 = "2023-10-05"
    try:
        result = is_date_earlier(sample_date1, sample_date2)
        print(f"{sample_date1} is earlier than {sample_date2}: {result}")
    except ValueError as e:
        print(e)