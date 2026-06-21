import re
from datetime import datetime

class LogParser:
    def __init__(self):
        self.logs = {}

    def parse_line(self, line):
        parts = line.split('|')
        if len(parts) != 3:
            return
        timestamp, level, message = parts
        date = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S').date()
        if date not in self.logs:
            self.logs[date] = []
        self.logs[date].append((level, message))

    def get_logs_by_date(self):
        return self.logs

if __name__ == '__main__':
    parser = LogParser()
    logs_data = """
2023-04-01 12:00:00|INFO|User logged in
2023-04-01 12:05:00|WARNING|Low disk space
2023-04-02 14:00:00|ERROR|Failed to load data
2023-04-02 14:05:00|INFO|User logged out
"""
    for line in logs_data.strip().split('\n'):
        parser.parse_line(line)
    
    print(parser.get_logs_by_date())