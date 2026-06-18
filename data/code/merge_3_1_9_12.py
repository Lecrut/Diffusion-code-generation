class WeightTracker:
    """A class to manage weight tracking statistics."""

    def __init__(self):
        self.weights = []  # List of weights in chronological order
        self.total_weight = 0
        self.max_weight = None
        self.min_weight = None
    
    def add_weight(self, entry_date: str, weight_kg: float) -> bool:
        """Adds a new weight entry and updates statistics.
        
        Args:
            entry_date (str): The date of the measurement as a string.
            weight_kg (float): The weight in kilograms.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            weight = float(weight_kg)
            self.weights.append({
                'date': entry_date,
                'weight': weight
            })
            
            # Update total and range statistics
            current_total = sum(w['weight'] for w in self.weights)
            if not self.max_weight or weight > self.max_weight:
                self.max_weight = weight
            if not self.min_weight or weight < self.min_weight:
                self.min_weight = weight
            
            # Recalculate total (though it should match the sum of list)
            self.total_weight = current_total
            
            return True
        except ValueError:
            print(f"Invalid weight value provided for date {entry_date}.")
            return False

    def get_statistics(self) -> dict:
        """Returns a dictionary containing all calculated statistics.
        
        Returns:
            dict: A dictionary with keys 'total', 'count', 'average', 
                 'max_weight', and 'min_weight'.
        """
        count = len(self.weights)
        if count == 0 or self.max_weight is None:
            return {
                "total": 0,
                "count": 0,
                "average": 0.0,
                "max_weight": None,
                "min_weight": None
            }

        average = self.total_weight / count
        
        return {
            "total": round(self.total_weight, 2),
            "count": count,
            "average": round(average, 2),
            "max_weight": round(self.max_weight, 2) if self.max_weight else None,
            "min_weight": round(self.min_weight, 2) if self.min_weight else None
        }

if __name__ == '__main__':
    # Initialize the tracker with hard-coded sample data to demonstrate functionality.
    # No user input, command-line arguments, or network access is required for this block.
    
    # Create an instance of WeightTracker
    my_tracker = WeightTracker()

    # Add initial sample weights directly via method calls since interactive I/O is forbidden.
    entry_1_date = "2023-09-01"
    entry_1_weight = 75.5
    
    entry_2_date = "2023-09-15"
    entry_2_weight = 74.8

    entry_3_date = "2023-10-01"
    entry_3_weight = 76.2

    # Add weights to the tracker (simulating user input logic internally)
    my_tracker.add_weight(entry_1_date, entry_1_weight)
    my_tracker.add_weight(entry_2_date, entry_2_weight)
    my_tracker.add_weight(entry_3_date, entry_3_weight)

    # Retrieve and display updated statistics
    stats = my_tracker.get_statistics()
    
    print("Weight Tracking Summary")
    print("-" * 25)
    print(f"Total Weights: {stats['total']} kg")
    print(f"Number of Entries: {stats['count']}")
    print(f"Average Weight: {stats['average']} kg")
    
    if stats['max_weight'] is not None and stats['min_weight'] is not None:
        print("-" * 25)
        print(f"Weight Range:")
        print(f"  Minimum: {stats['min_weight']} kg")
        print(f"  Maximum: {stats['max_weight']} kg")
    else:
        print("No weight range data available.")