from datetime import datetime

def get_day_from_timestamp(timestamp: str) -> int:
    try:
        date_object = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S")
        return date_object.day
    except ValueError as e:
        raise ValueError("Invalid timestamp format. Please use YYYY-MM-DDTHH:MM:SS.") from e

if __name__ == '__main__':
    timestamp1 = "2024-07-04T12:00:00"
    print(f"Day for {timestamp1}: {get_day_from_timestamp(timestamp1)}")