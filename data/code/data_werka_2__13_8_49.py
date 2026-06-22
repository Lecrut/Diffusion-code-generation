from typing import List

class TimeCalculator:
    def __init__(self):
        self.units = {
            'hour': 60,
            'minute': 1
        }

    def parse_time(self, time_str: str) -> int:
        total_minutes = 0
        parts = time_str.split()
        for i in range(0, len(parts), 2):
            value = int(parts[i])
            unit = parts[i + 1].lower().rstrip('s')
            if unit not in self.units:
                raise ValueError(f"Unsupported time unit: {unit}")
            total_minutes += value * self.units[unit]
        return total_minutes

    def calculate_total_time(self, time_differences: List[str]) -> int:
        return sum((self.parse_time(td) for td in time_differences))

if __name__ == '__main__':
    sample_times = ['2 hours 30 minutes', '1 hour 45 minutes', '30 minutes', '4 hours']
    calculator = TimeCalculator()
    total_time = calculator.calculate_total_time(sample_times)
    print(total_time)