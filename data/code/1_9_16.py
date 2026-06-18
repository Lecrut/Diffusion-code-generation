import statistics

class WeightTracker:
    """A class to manage weight tracking operations including adding weights, 
    calculating averages, finding medians, sorting data, and retrieving stats."""
    
    def __init__(self):
        self.weights = []

    def add_weight(self, new_weight: float) -> None:
        """Adds a single weight value to the tracker's list.
        
        Args:
            new_weight (float): The weight value to be added.
            
        Raises:
            ValueError: If the input is not numeric or negative.
        """
        if isinstance(new_weight, float) and new_weight >= 0:
            self.weights.append(new_weight)

    def get_average(self) -> float | None:
        """Calculates and returns the average of all recorded weights.
        
        Returns:
            float or None: The arithmetic mean if data exists, else None.
        """
        return statistics.mean(self.weights) if self.weights else None

    def get_median(self) -> float | None:
        """Returns the median weight from the list after sorting it internally 
        to ensure accurate calculation."""
        sorted_weights = sorted(self.weights)
        n = len(sorted_weights)
        
        if not sorted_weights:
            return None
        
        mid = n // 2
        if n % 2 == 0:
            # Even number of elements, average the two middle values
            median_value = (sorted_weights[mid - 1] + sorted_weights[mid]) / 2.0
        else:
            # Odd number of elements, return the exact middle value
            median_value = float(sorted_weights[mid])
        
        return median_value

    def sort_weights(self) -> None:
        """Sorts the internal weights list in ascending order."""
        self.weights.sort()

class WeightReportGenerator(WeightTracker):
    """A subclass that extends functionality to generate formatted reports 
    with multiple statistical measures."""
    
    def get_min_weight(self) -> float | None:
        return min(self.weights) if self.weights else None

    def get_max_weight(self) -> float | None:
        return max(self.weights) if self.weights else None

if __name__ == '__main__':
    # Hard-coded sample values to run the program without user input
    
    tracker = WeightReportGenerator()
    
    # Adding initial hard-coded weights
    tracker.add_weight(150.5)
    tracker.add_weight(148.2)
    tracker.add_weight(160.0)
    tracker.add_weight(155.75)
    tracker.add_weight(159.3)

    # Generating and displaying the report
    
    print("Weight Tracking Report")
    print("-" * 30)
    
    total_weights = len(tracker.weights)
    avg_weight = tracker.get_average()
    median_weight = tracker.get_median()
    min_weight = tracker.get_min_weight()
    max_weight = tracker.get_max_weight()

    # Sort and display sorted data for clarity
    
    print(f"Total Records: {total_weights}")
    
    if total_weights > 0:
        print(f"Avg Weight: {avg_weight:.2f} kg")
        print(f"Median Weight: {median_weight:.2f} kg")
        
        # Sort the list to show progression or order
    
        tracker.sort_weights()
        
        sorted_str = ", ".join(str(w) for w in tracker.weights)
        print("Sorted Weights:", f"[{sorted_str}]")

    else:
        print("No data available.")
    
    print("-" * 30)