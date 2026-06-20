from datetime import datetime

def is_weekday(iso_date_str):
    date_obj = datetime.fromisoformat(iso_date_str)
    return date_obj.weekday() < 5
if __name__ == '__main__':
    print(is_weekday('2023-10-02'))
    print(is_weekday('2023-10-07'))