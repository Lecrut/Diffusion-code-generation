from datetime import datetime

class ElapsedTimeFormatter:
    SEPARATOR = ':'
    FORMAT_SPEC = ':02d'
    SECONDS_PER_HOUR = 3600
    SECONDS_PER_MINUTE = 60

    def format_elapsed(self, start_time, end_time):
        total_seconds = int((end_time - start_time).total_seconds())
        hours = total_seconds // self.SECONDS_PER_HOUR
        remainder = total_seconds % self.SECONDS_PER_HOUR
        minutes = remainder // self.SECONDS_PER_MINUTE
        seconds = remainder % self.SECONDS_PER_MINUTE
        h_str = f"{hours}{self.FORMAT_SPEC}"
        m_str = f"{minutes}{self.FORMAT_SPEC}"
        s_str = f"{seconds}{self.FORMAT_SPEC}"
        return f"{h_str}{self.SEPARATOR}{m_str}{self.SEPARATOR}{s_str}"

if __name__ == '__main__':
    formatter = ElapsedTimeFormatter()
    now = datetime.now()
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    result = formatter.format_elapsed(start_of_day, now)
    print(result)