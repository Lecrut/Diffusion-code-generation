import re

class LogParser:
    def __init__(self):
        self.logs = {}

    def parse_line(self, line):
        parts = line.split('|')
        if len(parts) == 3:
            timestamp, level, message = parts
            date = timestamp.split(' ')[0]
            entry = {'level': level, 'message': message}
            if date in self.logs:
                self.logs[date].append(entry)
            else:
                self.logs[date] = [entry]

    def parse_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                self.parse_line(line.strip())

    def get_logs_by_date(self, date):
        return self.logs.get(date, [])

if __name__ == '__main__':
    parser = LogParser()
    parser.parse_line('2023-10-01 14:30:00|INFO|Starting application')
    parser.parse_line('2023-10-01 14:35:00|ERROR|Failed to connect')
    parser.parse_line('2023-10-02 09:00:00|INFO|Application running')

    print(parser.get_logs_by_date('2023-10-01'))
    print(parser.get_logs_by_date('2023-10-02'))
    print(parser.get_logs_by_date('2023-10-03'))