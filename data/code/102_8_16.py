from datetime import datetime

def is_weekday(iso_date: str) -> bool:
    date_obj = datetime.fromisoformat(iso_date)
    return date_obj.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-05'))
    print(is_weekday('2023-10-06'))