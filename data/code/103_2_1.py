class TimeCalculator:
    def get_elapsed_time(self):
        import datetime
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute
        hours = now.hour
        total_seconds = (now.hour * 3600) + (now.minute * 60) + now.second
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return hours, minutes, seconds
if __name__ == '__main__':
    calculator = TimeCalculator()
    hours, minutes, seconds = calculator.get_elapsed_time()
    print(f"Hours: {hours}, Minutes: {minutes}, Seconds: {seconds}")