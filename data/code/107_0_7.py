from datetime import datetime

def format_iso8601(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    iso_format_map = {
        'year': '%Y',
        'month': '%m',
        'day': '%d',
        'hour': '%H',
        'minute': '%M',
        'second': '%S'
    }
    formatted_parts = [dt.strftime(iso_format_map[key]) for key in iso_format_map]
    return f"{formatted_parts[0]}-{formatted_parts[1]}-{formatted_parts[2]} {formatted_parts[3]}:{formatted_parts[4]}:{formatted_parts[5]}"

if __name__ == '__main__':
    sample_datetime = datetime(2024, 1, 15, 8, 5, 9)
    formatted_str = format_iso8601(sample_datetime)
    print(formatted_str)