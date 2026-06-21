import re
from collections import defaultdict

def parse_logs(log_file):
    log_entries = defaultdict(list)
    date_pattern = r'\d{4}-\d{2}-\d{2}'
    
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' | ')
            if len(parts) == 3:
                timestamp, level, message = parts
                date_match = re.search(date_pattern, timestamp)
                if date_match:
                    date = date_match.group(0)
                    log_entries[date].append((timestamp, level, message))
    
    return dict(log_entries)

if __name__ == '__main__':
    sample_log_file = 'sample.log'
    logs_by_date = parse_logs(sample_log_file)
    print(logs_by_date)