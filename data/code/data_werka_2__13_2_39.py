from datetime import datetime

def calculate_total_elapsed_time(timestamps):
    if not timestamps:
        return 0
    
    def parse_timestamp(ts):
        return datetime.fromisoformat(ts)
    
    parsed_times = [parse_timestamp(ts) for ts in timestamps]
    earliest_time = min(parsed_times)
    latest_time = max(parsed_times)
    
    elapsed_seconds = (latest_time - earliest_time).total_seconds()
    return elapsed_seconds

if __name__ == '__main__':
    sample_timestamps = [
        "2023-05-01T08:00:00Z",
        "2023-05-03T17:45:00Z",
        "2023-05-02T12:15:00Z"
    ]
    
    total_time = calculate_total_elapsed_time(sample_timestamps)
    print(total_time)