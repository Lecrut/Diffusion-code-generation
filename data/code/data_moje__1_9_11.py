import statistics
from datetime import datetime
from typing import List, Optional

class WeightEntry:
    def __init__(self, weight_kg: float, date: Optional[datetime] = None):
        if date is None:
            date = datetime.now()
        self.weight_kg = weight_kg
        self.date = date

    def __repr__(self):
        return f"WeightEntry(weight_kg={self.weight_kg}, date={self.date})"

class WeightTracker:
    def __init__(self):
        self.entries: List[WeightEntry] = []

    def add_weight(self, weight_kg: float, date: Optional[datetime] = None) -> None:
        if weight_kg <= 0:
            raise ValueError("Weight must be positive")
        entry = WeightEntry(weight_kg, date)
        self.entries.append(entry)

    def get_statistics(self) -> dict:
        if not self.entries:
            return {
                "count": 0,
                "mean": None,
                "median": None,
                "min": None,
                "max": None,
                "stdev": None,
                "latest": None
            }

        weights = [entry.weight_kg for entry in self.entries]
        latest_entry = self.entries[-1]

        return {
            "count": len(weights),
            "mean": statistics.mean(weights),
            "median": statistics.median(weights),
            "min": min(weights),
            "max": max(weights),
            "stdev": statistics.stdev(weights) if len(weights) > 1 else 0.0,
            "latest": latest_entry.weight_kg
        }

    def get_recent_entries(self, n: int = 5) -> List[WeightEntry]:
        return self.entries[-n:] if len(self.entries) >= n else self.entries[:]

    def calculate_trend(self) -> Optional[float]:
        if len(self.entries) < 2:
            return None
        first_weight = self.entries[0].weight_kg
        last_weight = self.entries[-1].weight_kg
        return last_weight - first_weight

def format_statistics(stats: dict) -> str:
    lines = []
    lines.append(f"Weight Tracking Statistics")
    lines.append(f"=========================")
    lines.append(f"Number of entries: {stats['count']}")
    if stats['mean'] is not None:
        lines.append(f"Mean weight: {stats['mean']:.2f} kg")
        lines.append(f"Median weight: {stats['median']:.2f} kg")
        lines.append(f"Minimum weight: {stats['min']:.2f} kg")
        lines.append(f"Maximum weight: {stats['max']:.2f} kg")
        lines.append(f"Standard deviation: {stats['stdev']:.2f} kg")
        lines.append(f"Latest weight: {stats['latest']:.2f} kg")
    else:
        lines.append("No data available")
    return "\n".join(lines)

if __name__ == '__main__':
    tracker = WeightTracker()

    sample_dates = [
        datetime(2024, 1, 1),
        datetime(2024, 2, 1),
        datetime(2024, 3, 1),
        datetime(2024, 4, 1),
        datetime(2024, 5, 1),
    ]

    sample_weights = [85.5, 84.8, 85.1, 83.9, 83.2]

    for weight, date in zip(sample_weights, sample_dates):
        tracker.add_weight(weight, date)

    stats = tracker.get_statistics()
    print(format_statistics(stats))

    trend = tracker.calculate_trend()
    print(f"Trend: {trend:.2f} kg")

    recent = tracker.get_recent_entries(3)
    for entry in recent:
        print(entry)