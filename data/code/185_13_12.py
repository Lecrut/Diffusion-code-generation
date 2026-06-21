import re
from datetime import datetime

LOG_PATTERN = re.compile(r'(\d{4}-\d{2}-\d{2}) \| (\w+) \| (.*)')

def parse_log_line(line):
    match = LOG_PATTERN.match(line)
    if match:
        date_str, level, message = match.groups()
        return datetime.strptime(date_str, '%Y-%m-%d'), level, message
    return None

def group_logs_by_date(log_lines):
    logs_by_date = {}
    for line in log_lines:
        parsed_line = parse_log_line(line)
        if parsed_line:
            date, _, _ = parsed_line
            date_key = date.strftime('%Y-%m-%d')
            if date_key not in logs_by_date:
                logs_by_date[date_key] = []
            logs_by_date[date_key].append(parsed_line)
    return logs_by_date

if __name__ == '__main__':
    sample_logs = [
        "2023-10-01 | INFO | User logged in",
        "2023-10-01 | ERROR | Failed to load data",
        "2023-10-02 | INFO | User logged out",
        "2023-10-02 | INFO | User logged in"
    ]
    grouped_logs = group_logs_by_date(sample_logs)
    print(grouped_logs)