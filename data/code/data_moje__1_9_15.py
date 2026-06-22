class WeightEntry:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a number")
        if value <= 0:
            raise ValueError("Weight must be positive")
        self.value = value

class StatisticsCalculator:
    def calculate_mean(self, numbers):
        if not numbers:
            return 0.0
        return sum(numbers) / len(numbers)

    def calculate_min(self, numbers):
        if not numbers:
            return None
        return min(numbers)

    def calculate_max(self, numbers):
        if not numbers:
            return None
        return max(numbers)

    def calculate_median(self, numbers):
        if not numbers:
            return None
        sorted_nums = sorted(numbers)
        n = len(sorted_nums)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0
        return sorted_nums[mid]

class WeightSystem:
    def __init__(self):
        self.entries = []
        self.calculator = StatisticsCalculator()

    def record_weight(self, weight):
        entry = WeightEntry(weight)
        self.entries.append(entry)
        return entry.value

    def get_current_stats(self):
        values = [e.value for e in self.entries]
        if not values:
            return {
                "count": 0,
                "mean": None,
                "min": None,
                "max": None,
                "median": None
            }
        return {
            "count": len(values),
            "mean": self.calculator.calculate_mean(values),
            "min": self.calculator.calculate_min(values),
            "max": self.calculator.calculate_max(values),
            "median": self.calculator.calculate_median(values)
        }

if __name__ == '__main__':
    system = WeightSystem()
    system.record_weight(80.5)
    system.record_weight(79.2)
    system.record_weight(81.0)
    system.record_weight(78.8)
    system.record_weight(80.1)
    stats = system.get_current_stats()
    print(stats)