from typing import List

class TimeParser:

    def __init__(self):
        self.unit_map = {'hour': 60, 'minute': 1}

    def parse_time_difference(self, time_str: str) -> int:
        total_minutes = 0
        parts = time_str.split()
        for i in range(0, len(parts), 2):
            value = int(parts[i])
            unit = parts[i + 1].lower().rstrip('s')
            if unit in self.unit_map:
                total_minutes += value * self.unit_map[unit]
            else:
                raise ValueError(f'Unsupported time unit: {unit}')
        return total_minutes

def total_elapsed_time(time_differences: List[str]) -> int:
    parser = TimeParser()
    total_time = sum((parser.parse_time_difference(td) for td in time_differences))
    return total_time
if __name__ == '__main__':
    sample_times = ['5 hours 20 minutes', '3 hours', '1 hour 5 minutes', '40 minutes']
    total_time = total_elapsed_time(sample_times)
    print(total_time)