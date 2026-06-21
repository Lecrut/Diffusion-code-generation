from collections import defaultdict
import re

def parse_logs(log_file):
    log_entries = defaultdict(list)
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            if len(parts) == 3:
                timestamp, level, message = parts
                date_match = re.search(date_pattern, timestamp)
                if date_match:
                    date = date_match.group()
                    log_entries[date].append((timestamp, level, message))
    
    return dict(log_entries)

if __name__ == '__main__':
    sample_log_content = """2023-10-01|INFO|System started
2023-10-01|ERROR|Disk space low
2023-10-02|INFO|Backup completed
2023-10-01|WARNING|Resource usage high"""
    
    with open('sample_log.txt', 'w') as file:
        file.write(sample_log_content)
    
    logs = parse_logs('sample_log.txt')
    print(logs)