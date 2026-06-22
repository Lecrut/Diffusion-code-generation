from datetime import datetime

def is_first_date_earlier(reference_date: datetime, comparison_date: datetime) -> bool:
    timestamp_reference = reference_date.timestamp()
    timestamp_comparison = comparison_date.timestamp()
    return timestamp_reference < timestamp_comparison

if __name__ == '__main__':
    start_time = datetime(2024, 5, 15, 8, 30, 0)
    end_time = datetime(2024, 5, 15, 9, 45, 0)
    is_earlier = is_first_date_earlier(start_time, end_time)
    print(is_earlier)