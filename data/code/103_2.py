class TimeCalculator:
    def get_elapsed_time(self):
        import datetime
        now = datetime.datetime.now()
        total_seconds = now.hour * 3600 + now.minute * 60 + now.second
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        return hours, minutes, seconds
if __name__ == '__main__':
    calculator = TimeCalculator()
    hours, minutes, seconds = calculator.get_elapsed_time()
    print(f"Elapsed time for the current day: {hours} hours, {minutes} minutes, and {seconds} seconds")