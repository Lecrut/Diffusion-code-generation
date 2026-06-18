import json
from typing import Dict, Tuple, Optional

class WeightPairDictionary:
    """
    A dictionary-based solution to store multiple weight pairs 
    and provide a function to quickly retrieve the difference between any two stored weights.
    
    Attributes:
        storage (Dict[Tuple[float, float], None]): Internal key-value map for O(1) access.
            Keys are tuples of (weight_a, weight_b). Values can be arbitrary data if needed later.
        
        differences_cache (Optional[Dict[str, float]]): Optional cache to store computed 
            differences indexed by a unique string identifier derived from the tuple keys.

    Methods:
        add_pair(weight_a: float, weight_b: float) -> None: Adds or updates a pair of weights.
        get_difference(key_identifier: str) -> Optional[float]: Retrieves pre-computed difference for given key_id.
    
    Example usage (inside __main__):
        w = WeightPairDictionary()
        w.add_pair(10, 5)
        print(w.get_difference("pair_1")) # Outputs the calculated difference if cached or computed on demand logic is applied
    """

    def __init__(self):
        self.storage: Dict[Tuple[float, float], object] = {}
        # We will compute differences internally when requested for a unique key_id derived from sorted tuple to ensure uniqueness regardless of order.

    def _generate_key(self, weight_a: float, weight_b: float) -> str:
        """Generates a canonical string key based on the pair (min_weight, max_weight)."""
        return f"pair_{int(min(weight_a, weight_b))}_{max(int(weight_a), int(weight_b))}"

    def add_pair(self, weight_a: float, weight_b: float) -> None:
        """Adds a new weight pair to the dictionary."""
        # Ensure weights are stored as floats for precision but use integer parts for canonical key generation if desired.
        self.storage[(weight_a, weight_b)] = "uninitialized"

    def get_difference(self, weight_a: float, weight_b: float) -> Optional[float]:
        """
        Retrieves the absolute difference between two weights stored in the dictionary.
        
        Args:
            weight_a (float): First weight value.
            weight_b (float): Second weight value.

        Returns:
            Optional[float]: The absolute difference if both values exist and match a stored pair, else None.
            
            Note: Since floating point comparisons can be tricky, we will check for exact tuple match in storage keys first.
              If the user wants tolerance-based matching, it would require more complex logic not explicitly requested here 
              to keep 'quickly retrieve' efficient without external libraries like numpy or scipy.
        """
        
        # Check if this exact pair exists (order matters in dict key) OR check reverse order for robustness?
        # The prompt asks for "difference for any stored pair", implying we match the tuple provided. 
        # However, to be safe and useful, let's try both orders of input keys against our internal storage.

        target_key = (weight_a, weight_b)
        
        if target_key in self.storage:
            return abs(weight_a - weight_b)
            
        # Fallback check for reversed order just in case the user passes unordered inputs referring to same pair
        reverse_target_key = (weight_b, weight_a)
        if reverse_target_key in self.storage:
             return abs(weight_a - weight_b)

        return None

def main():
    """Main execution block with hard-coded sample values."""
    
    # Initialize the dictionary solution
    w_dict = WeightPairDictionary()

    # Add some hardcoded pairs as per task requirements (no input prompts, no files, etc.)
    pair_1 = 50.5
    pair_2 = 30.0
    pair_3 = 8.7
    
    print("Adding sample weight pairs...")
    
    w_dict.add_pair(pair_1, pair_2) # Stores (50.5, 30.0) -> diff is |20.5|
    w_dict.add_pair(45.0, pair_2)   # Stores (45.0, 30.0) -> diff is |15.0|
    
    print("Pairs added successfully.")

    # Retrieve differences for specific pairs using the helper function logic directly on inputs
    
    result_a = w_dict.get_difference(pair_1, pair_2)
    result_b = w_dict.get_difference(45.0, 30.0)
    
    print(f"Difference between {pair_1} and {pair_2}: {result_a}")
    print(f"Difference between 45.0 and {pair_2}: {result_b}")

    # Demonstrate retrieval on non-existent pair to show None behavior
    result_non_existent = w_dict.get_difference(99.9, 1.1)
    if result_non_existent is None:
        print("Difference for unknown pair (99.9, 1.1): Not found in storage.")

if __name__ == '__main__':
    main()