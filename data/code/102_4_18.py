from datetime import datetime

def validate_weekday(timestamp: str) -> bool:
    parsed_dt = datetime.fromisoformat(timestamp)
    day_index = parsed_dt.weekday()
    is_weekday = day_index < 5
    return is_weekday

if __name__ == '__main__':
    test_ts = '2024-12-25T09:00:00'
    validation_result = validate_weekday(test_ts)
    print(validation_result)