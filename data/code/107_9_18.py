import calendar

def transform_date(source: str) -> str:
    if not isinstance(source, str):
        raise ValueError("Input must be a string")
    segments = source.split('-')
    if len(segments) != 3:
        raise ValueError("Expected three segments")
    try:
        y = int(segments[0])
        m = int(segments[1])
        d = int(segments[2])
    except ValueError:
        raise ValueError("Numeric components required")
    if not (1 <= m <= 12):
        raise ValueError("Invalid month")
    month_label = calendar.month_name[m]
    return f"{month_label} {d:02d}, {y}"

if __name__ == '__main__':
    print(transform_date('2023-1-5'))
    print(transform_date('2024-12-25'))
    print(transform_date('2000-2-29'))