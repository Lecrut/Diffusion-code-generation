def parse_log_line(line):
    parts = line.split(' | ')
    if len(parts) != 3:
        raise ValueError("Invalid log format")
    timestamp, level, message = parts
    date = timestamp.split()[0]
    return date, (level, message)

def group_logs_by_date(log_lines):
    result = {}
    for line in log_lines:
        try:
            date, log_entry = parse_log_line(line)
            if date not in result:
                result[date] = []
            result[date].append(log_entry)
        except ValueError as e:
            print(f"Skipping invalid log line: {e}")
    return result

if __name__ == '__main__':
    sample_logs = [
        "2023-10-01 14:30:00 | INFO | User logged in",
        "2023-10-01 15:45:00 | ERROR | Failed to load data",
        "2023-10-02 09:15:00 | INFO | Data loaded successfully"
    ]
    grouped_logs = group_logs_by_date(sample_logs)
    print(grouped_logs)