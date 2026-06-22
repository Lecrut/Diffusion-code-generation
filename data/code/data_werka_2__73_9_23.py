from datetime import datetime, timedelta

DATE_FORMAT = '%Y-%m-%d'
SECONDS_PER_DAY = 86400

def compute_date_span(start: str, end: str) -> int:
    parsed_start = datetime.strptime(start, DATE_FORMAT)
    parsed_end = datetime.strptime(end, DATE_FORMAT)
    time_delta = parsed_end - parsed_start
    total_seconds = time_delta.total_seconds()
    return int(total_seconds / SECONDS_PER_DAY)

if __name__ == '__main__':
    initial_date = '2020-01-01'
    final_date = '2020-12-31'
    span_result = compute_date_span(initial_date, final_date)
    print(span_result)