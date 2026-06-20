from datetime import datetime

def dates_in_same_week(date1_str: str, date2_str: str) -> bool:
    date_format = '%Y-%m-%d'
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    return date1.isocalendar()[1] == date2.isocalendar()[1]

if __name__ == '__main__':
    sample_date1 = "2023-12-25"
    sample_date2 = "2023-12-31"
    result = dates_in_same_week(sample_date1, sample_date2)
    print(f"Are {sample_date1} and {sample_date2} in the same week? {result}")