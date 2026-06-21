from datetime import datetime

class ISOFormatter:
    def __init__(self, dt):
        self.dt = dt

    def to_string(self):
        parts = [
            str(self.dt.year),
            str(self.dt.month).zfill(2),
            str(self.dt.day).zfill(2),
            str(self.dt.hour).zfill(2),
            str(self.dt.minute).zfill(2),
            str(self.dt.second).zfill(2)
        ]
        return f"{parts[0]}-{parts[1]}-{parts[2]} {parts[3]}:{parts[4]}:{parts[5]}"

    def get_date_part(self):
        return f"{self.dt.year}-{self.dt.month:02d}-{self.dt.day:02d}"

    def get_time_part(self):
        return f"{self.dt.hour:02d}:{self.dt.minute:02d}:{self.dt.second:02d}"

if __name__ == '__main__':
    now = datetime(2024, 12, 25, 9, 30, 45)
    formatter = ISOFormatter(now)
    print(formatter.to_string())
    print(formatter.get_date_part())
    print(formatter.get_time_part())
    
    past = datetime(2021, 1, 1, 0, 0, 1)
    past_formatter = ISOFormatter(past)
    print(past_formatter.to_string())