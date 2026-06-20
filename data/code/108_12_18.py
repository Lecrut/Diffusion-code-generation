from datetime import datetime

def get_day_of_month(date_string: str) -> int:
    date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
    return date_object.day

if __name__ == '__main__':
    sample_date = "2024-07-04T12:00:00"
    print(f"Day of the month for {sample_date}: {get_day_of_month(sample_date)}")