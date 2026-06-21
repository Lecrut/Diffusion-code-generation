from collections import defaultdict

def parse_logs(log_file):
    logs_by_date = defaultdict(list)
    for line in log_file:
        timestamp, level, message = line.strip().split('|')
        date = timestamp.split()[0]
        logs_by_date[date].append((timestamp, level, message))
    return dict(logs_by_date)

if __name__ == '__main__':
    sample_logs = """2023-10-01 12:00:00|INFO|System started
2023-10-01 12:05:00|ERROR|Failed to connect
2023-10-02 14:00:00|INFO|System restarted
2023-10-02 14:05:00|WARNING|Low disk space"""
    logs = parse_logs(sample_logs.splitlines())
    print(logs)