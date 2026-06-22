class TimeCalculator:
    UNIT_MAPPING = {
        'hour': 60,
        'minute': 1
    }

    @staticmethod
    def parse_time_difference(time_str):
        total_minutes = 0
        parts = time_str.split()
        for i in range(0, len(parts), 2):
            value = int(parts[i])
            unit = parts[i + 1].lower().rstrip('s')
            if unit not in TimeCalculator.UNIT_MAPPING:
                raise ValueError(f"Unsupported time unit: {unit}")
            total_minutes += value * TimeCalculator.UNIT_MAPPING[unit]
        return total_minutes

    @staticmethod
    def total_elapsed_time(time_differences):
        return sum(TimeCalculator.parse_time_difference(td) for td in time_differences)

if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '4 hours']
    total_time = TimeCalculator.total_elapsed_time(sample_times)
    print(total_time)