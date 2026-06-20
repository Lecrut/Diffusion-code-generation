from datetime import datetime

def calculate_date_difference(date1_str: str, date2_str: str) -> int:
    date1 = datetime.strptime(date1_str, '%Y-%m-%d')
    date2 = datetime.strptime(date2_str, '%Y-%m-%d')
    return (date2 - date1).days

if __name__ == '__main__':
    sample_dates = {
        "start_date": "2023-01-01",
        "end_date": "2023-01-10"
    }
    difference = calculate_date_difference(sample_dates["start_date"], sample_dates["end_date"])
    print(f"Date difference: {difference} days")