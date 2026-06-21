from collections import defaultdict

def parse_logs(log_file):
    logs_by_date = defaultdict(list)
    for line in log_file:
        timestamp, level, message = line.strip().split('|')
        date = timestamp.split()[0]
        logs_by_date[date].append((timestamp, level, message))
    return dict(logs_by_date)

if __name__ == '__main__':
    sample_logs = [
        "2023-10-01 14:30:00|INFO|User logged in",
        "2023-10-01 15:45:00|ERROR|Failed to load data",
        "2023-10-02 09:15:00|INFO|System rebooted",
    ]
    print(parse_logs(sample_logs))