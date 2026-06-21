from collections import defaultdict

def parse_logs(log_file):
    log_dict = defaultdict(list)
    for line in log_file:
        timestamp, level, message = line.strip().split(' | ')
        date = timestamp.split()[0]
        log_dict[date].append((level, message))
    return dict(log_dict)

if __name__ == '__main__':
    sample_log = [
        "2023-10-01 14:30:00 | INFO | User logged in",
        "2023-10-01 14:35:00 | ERROR | Failed to load resource",
        "2023-10-02 10:00:00 | INFO | System rebooted"
    ]
    print(parse_logs(sample_log))