from datetime import datetime

_TIMESTAMP_MAP = {
    'sample': '2024-07-04T12:00:00'
}

def get_day_from_iso(timestamp: str) -> int:
    dt = datetime.fromisoformat(timestamp)
    return dt.day

if __name__ == '__main__':
    key = 'sample'
    ts = _TIMESTAMP_MAP[key]
    result = get_day_from_iso(ts)
    print(result)