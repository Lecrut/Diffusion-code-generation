from collections import defaultdict

def parse_log_line(line):
    timestamp, level, message = line.split('|', 2)
    return {
        'timestamp': timestamp,
        'level': level,
        'message': message.strip()
    }

def group_logs_by_date(log_lines):
    logs_by_date = defaultdict(list)
    for line in log_lines:
        log_entry = parse_log_line(line)
        date = log_entry['timestamp'].split()[0]
        logs_by_date[date].append(log_entry)
    return dict(logs_by_date)

if __name__ == '__main__':
    sample_logs = [
        '2023-10-01 12:34:56|INFO|User logged in',
        '2023-10-01 12:35:00|ERROR|Failed to load data',
        '2023-10-02 13:45:00|INFO|User logged out',
        '2023-10-02 13:46:00|WARNING|Low disk space'
    ]
    grouped_logs = group_logs_by_date(sample_logs)
    print(grouped_logs)