from collections import defaultdict
import re

def parse_logs(log_file):
    log_dict = defaultdict(list)
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                timestamp, level, message = parts
                date_match = re.match(date_pattern, timestamp)
                if date_match:
                    date = date_match.group()
                    log_dict[date].append((timestamp, level, message))
    
    return dict(log_dict)

if __name__ == '__main__':
    sample_logs = """
2023-10-01|INFO|System started
2023-10-01|ERROR|Disk space low
2023-10-02|INFO|Backup completed
2023-10-01|WARNING|Resource usage high
"""
    with open('sample.log', 'w') as file:
        file.write(sample_logs)
    
    logs = parse_logs('sample.log')
    print(logs)