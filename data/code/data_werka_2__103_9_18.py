from datetime import datetime, time

class TimeCalculator:
    def __init__(self, reference_dt=None):
        self.reference_dt = reference_dt if reference_dt is not None else datetime.now()

    def get_elapsed_since_midnight(self):
        midnight = datetime.combine(self.reference_dt.date(), time.min)
        delta = self.reference_dt - midnight
        total_seconds = int(delta.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    def get_reference_time(self):
        return self.reference_dt

if __name__ == '__main__':
    calc = TimeCalculator()
    print(calc.get_elapsed_since_midnight())
    print(calc.get_reference_time())