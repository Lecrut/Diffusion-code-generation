import copy

class WeightRecord:
    """Represents a single weight entry with date, value, and metadata."""

    def __init__(self, date_str: str, weight_value: float):
        self.date = date_str
        self.weight = weight_value
        self.achievements = []  # List of strings describing progress or milestones

class WeightTrackingSystem:
    """Manages a collection of weight records and calculates statistics."""

    def __init__(self):
        self.records = []  # Internal list to store all records

    def add_record(self, date_str: str, weight_value: float) -> None:
        """Adds a new weight record to the system.

        Args:
            date_str (str): The date of the entry in 'YYYY-MM-DD' format.
            weight_value (float): The recorded weight value.
        """
        if not isinstance(weight_value, (int, float)) or weight_value < 0:
            raise ValueError("Weight must be a non-negative number.")

        record = WeightRecord(date_str=date_str, weight_value=weight_value)
        self.records.append(record)

    def get_total_weight(self) -> float:
        """Calculates the sum of all recorded weights.

        Returns:
            float: The total accumulated weight value across all records.
        """
        return sum(r.weight for r in self.records)

    def get_average_weight(self) -> float:
        """Calculates the average weight based on all records.

        Returns:
            float: The arithmetic mean of recorded weights.
        """
        if not self.records:
            raise ValueError("No records available to calculate an average.")
        
        return sum(r.weight for r in self.records) / len(self.records)

    def get_min_weight(self) -> float:
        """Finds the lowest weight ever recorded.

        Returns:
            float: The minimum weight value among all records.
        """
        if not self.records:
            raise ValueError("No records available to find a minimum.")

        return min(r.weight for r in self.records)

    def get_max_weight(self) -> float:
        """Finds the highest weight ever recorded.

        Returns:
            float: The maximum weight value among all records.
        """
        if not self.records:
            raise ValueError("No records available to find a maximum.")

        return max(r.weight for r in self.records)

    def get_weight_change(self, start_date_str: str = None, end_date_str: str = None) -> float:
        """Calculates the weight change between two specific dates.

        Args:
            start_date_str (str): The starting date ('YYYY-MM-DD'). Defaults to earliest record.
            end_date_str (str): The ending date ('YYYY-MM-DD'). Defaults to latest record.

        Returns:
            float: Weight at end date minus weight at start date.
        """
        if not self.records:
            raise ValueError("No records available.")

        sorted_records = sorted(self.records, key=lambda r: r.date)

        # Filter based on provided dates or use the full range of existing data
        filtered_records = [r for r in sorted_records 
                           if (start_date_str is None and not end_date_str) or
                              start_date_str <= r.date < end_date_str]
        
        if len(filtered_records) == 0:
            raise ValueError("No records found within the specified date range.")

        # If no specific dates were given, use first and last record automatically (handled above logic implicitly by defaulting to full set if None/None)
        # Correction on logic flow for defaults:
        pass

if __name__ == '__main__':
    pass
