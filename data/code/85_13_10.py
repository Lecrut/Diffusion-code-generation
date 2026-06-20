from datetime import datetime

def calculate_week_difference(date_str1: str, date_str2: str) -> int:
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        delta = abs((date2 - date1).days)
        weeks = delta // 7
        return weeks
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    sample_date1 = "2023-04-01"
    sample_date2 = "2023-05-15"
    result = calculate_week_difference(sample_date1, sample_date2)
    print(f"The difference between {sample_date1} and {sample_date2} is {result} weeks.")