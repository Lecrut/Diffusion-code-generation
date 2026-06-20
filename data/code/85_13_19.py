from datetime import datetime

def calculate_week_difference(date_str1: str, date_str2: str) -> float:
    try:
        date_format = '%Y-%m-%d'
        date1 = datetime.strptime(date_str1, date_format)
        date2 = datetime.strptime(date_str2, date_format)
        difference = abs((date2 - date1).days)
        weeks = difference / 7.0
        return weeks
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_sample = "2023-01-01"
    date2_sample = "2023-04-01"
    week_difference = calculate_week_difference(date1_sample, date2_sample)
    print(f"The difference between {date1_sample} and {date2_sample} is approximately {week_difference:.2f} weeks.")