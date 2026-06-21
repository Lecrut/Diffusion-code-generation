from collections import defaultdict

def parse_logs(log_file):
    logs_by_date = defaultdict(list)
    for line in log_file:
        timestamp, level, message = line.strip().split(' | ')
        date = timestamp.split()[0]
        logs_by_date[date].append((level, message))
    return dict(logs_by_date)

if __name__ == '__main__':
    sample_log_data = """2023-10-01 14:30:00 | INFO | User logged in
2023-10-01 15:45:00 | ERROR | Failed to load resource
2023-10-02 10:00:00 | INFO | System rebooted
2023-10-02 11:15:00 | WARNING | Low disk space"""
    logs = parse_logs(sample_log_data.splitlines())
    print(logs)