from datetime import datetime

def is_date_before(date1: str, date2: str) -> bool:
    date_format = "%Y-%m-%d"
    try:
        return datetime.strptime(date1, date_format) < datetime.strptime(date2, date_format)
    except ValueError:
        raise ValueError("Error: Invalid date format provided.")

if __name__ == '__main__':
    sample_date1 = "2023-11-15"
    sample_date2 = "2023-12-05"
    try:
        result = is_date_before(sample_date1, sample_date2)
        print(f"Is '{sample_date1}' before '{sample_date2}': {result}")
    except ValueError as e:
        print(e)