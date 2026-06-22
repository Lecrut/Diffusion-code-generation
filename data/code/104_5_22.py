from datetime import datetime

RESULT_MAP = {
    -1: "First is earlier",
    0: "They are equal",
    1: "Second is earlier",
}

def compare_datetimes(dt1: datetime, dt2: datetime) -> str:
    diff = (dt1 - dt2).total_seconds()
    sign = (diff > 0) - (diff < 0)
    return RESULT_MAP[sign]

if __name__ == '__main__':
    first = datetime(2024, 5, 10, 8, 30, 0)
    second = datetime(2024, 5, 10, 8, 30, 0)
    output = compare_datetimes(first, second)
    print(output)