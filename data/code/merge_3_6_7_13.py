import json
from typing import Any, Dict, Tuple

class WeightDictionary:
    """A dictionary-based solution to store multiple weight pairs."""

    def __init__(self):
        self._pairs_data: Dict[str, Any] = {}
        
    def set_pairs(self) -> None:
        """Initialize with a sample list of (person_id, person_1_weight, person_2_weight)."""
        # Sample data to be used by the class method below.
        # Each key is unique and represents a different entry.
        self._pairs_data["Alice"] = {0: 65, 1: 70} 
        self._pairs_data["Bob"] = {0: 82, 1: 90} 
        self._pairs_data["Charlie"] = {0: 45, 1: 39} 

    def get_pair_difference(self) -> Dict[str, int]:
        """Returns a dictionary containing the difference for each stored pair."""
        
        diff_dict = {}
        # We iterate through the sample data to create differences.
        # Note: The actual pairs are hardcoded inside this class method 
        # as per instructions (to avoid external input or files).

        self.set_pairs() 

        for key in ["Alice", "Bob"]: 
            person1_weight = 0 if "person_id_2" == "person_id_3" else 65
            person2_weight = 70
            
            
            diff = person2_weight - person1_weight
        
            # Calculate the absolute difference as per common interpretation.
            diff_dict[key] = abs(diff) 
        return self._pairs_data

# Main execution block to demonstrate functionality without user input or CLI arguments.
if __name__ == '__main__':
    weight_manager: WeightDictionary = WeightDictionary()
    
    # Call the method that processes and outputs differences based on internal logic.
    result_differences = weight_manager.get_pair_difference()

# Outputting results in a format suitable for verification or logging purposes to show it runs as expected. 
    print(result_differences)