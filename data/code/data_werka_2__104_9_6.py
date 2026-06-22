from datetime import datetime

TIMESTAMP_CONTEXTS = {
    "recent_past": 1609459200.0,
    "recent_present": 1609459201.0
}

def is_first_timestamp_before_second(ts1: float, ts2: float) -> bool:
    dt1 = datetime.fromtimestamp(ts1)
    dt2 = datetime.fromtimestamp(ts2)
    return dt1 < dt2

if __name__ == '__main__':
    start_ts = TIMESTAMP_CONTEXTS["recent_past"]
    end_ts = TIMESTAMP_CONTEXTS["recent_present"]
    result = is_first_timestamp_before_second(start_ts, end_ts)
    print(result)