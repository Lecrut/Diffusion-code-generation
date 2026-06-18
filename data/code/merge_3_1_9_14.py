class WeightRecord:
    """Represents a single weight measurement entry."""
    
    def __init__(self, date: str, weight_kg: float):
        self.date = date.strip() if isinstance(date, str) else ""
        self.weight = float(weight_kg) if isinstance(weight_kg, (int, float)) else 0.0

    @property
    def formatted_date(self) -> str:
        """Returns the date in a readable format."""
        return f"{self.date}"

    def __repr__(self):
        return f"WeightRecord(date='{self.formatted_date}', weight={self.weight}kg)"

class WeightStats:
    """Calculates and tracks statistical data about weights over time."""

    @staticmethod
    def calculate_average(weights_list) -> float:
        if not weights_list:
            return 0.0
        return sum(weights_list) / len(weights_list)

if __name__ == '__main__':
    pass
