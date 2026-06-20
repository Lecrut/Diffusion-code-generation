class TimeCalculator:
    SECONDS_PER_HOUR = 3600

    @staticmethod
    def elapsed_time_in_hours(start_time: str, end_time: str) -> float:
        start_parts = list(map(int, start_time.split(':')))
        end_parts = list(map(int, end_time.split(':')))

        start_seconds = sum(part * (60 ** power) for power, part in enumerate(reversed(start_parts)))
        end_seconds = sum(part * (60 ** power) for power, part in enumerate(reversed(end_parts)))

        return (end_seconds - start_seconds) / TimeCalculator.SECONDS_PER_HOUR

if __name__ == '__main__':
    time_calc = TimeCalculator()
    elapsed_hours = time_calc.elapsed_time_in_hours("12:30", "15:45")
    print(f"Elapsed Time in Hours: {elapsed_hours}")