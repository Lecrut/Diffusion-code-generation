import json
from typing import Dict, Tuple

class WeightPairStore:
    """
    A dictionary-based solution to store multiple weight pairs (in kg) 
    and provide a function to quickly retrieve the difference for any stored pair.
    
    Attributes:
        data_store (Dict[Tuple[int, int], float]): Internal storage mapping 
            tuples of (person_id_1, person_id_2) to the calculated weight difference in kg.
    """

    def __init__(self):
        # Initialize internal dictionary for storing pre-calculated differences.
        self.data_store: Dict[Tuple[int, int], float] = {}

    def store_pair(self, id_a: int, id_b: int, weight_a: float, weight_b: float) -> None:
        """
        Stores a new pair of individuals with their respective weights and calculates the difference.
        
        Args:
            id_a (int): Unique identifier for individual A.
            id_b (int): Unique identifier for individual B.
            weight_a (float): Weight in kg for individual A.
            weight_b (float): Weight in kg for individual B.
            
        Note: The difference is calculated as abs(weight_a - weight_b). If the pair 
              already exists, this method updates or ignores based on typical dictionary behavior;
              however, to ensure deterministic test results without side effects of overwrites,
              we assume pairs are unique in usage or simply overwrite if duplicate keys exist.
        """
        key = (id_a, id_b)
        difference = abs(weight_a - weight_b)
        
        # Using get with a default value handles potential existing entries gracefully for this task context.
        self.data_store[key] = round(difference, 2)

    def retrieve_difference(self, id_1: int, id_2: int) -> float | None:
        """
        Retrieves the stored weight difference between two individuals using a dictionary lookup.
        
        Args:
            id_1 (int): Unique identifier for individual 1.
            id_2 (int): Unique identifier for individual 2.
            
        Returns:
            float | None: The calculated weight difference in kg if found, otherwise None.
                         Note: Order of IDs does not matter due to tuple set logic used internally 
                         if implemented via sets, but here we use a simple dict key (id_1, id_2).
                         To make it robust against order (e.g., retrieving for (B, A)), the lookup
                         can check both permutations. This implementation checks direct match first.
        """
        # Attempt to retrieve with specific ID order provided by user if unique per call logic is assumed strict
        key = (id_1, id_2)
        
        # Optimization: Check reverse key as well for robustness against input ordering variations
        reversed_key = (id_2, id_1)
        
        return self.data_store.get(key) or self.data_store.get(reversed_key)

    def get_all_pairs(self) -> list[Tuple[int, int]]:
        """Returns a sorted list of all stored ID pairs as tuples."""
        # Sorting keys ensures consistent output order for debugging/verification
        return [key for key in sorted(self.data_store.keys())]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    
    store = WeightPairStore()

    # Sample pairs of individuals and their weights (in kg)
    samples = [
        ("Alice", 70),   # ID: Alice, Weight: 70kg -> We'll map names to IDs internally? 
                         # Let's use simple integer IDs for this specific task requirement.
                        ]

    # Redefining sample data with explicit integers as per typical dictionary key usage requirements in such tasks
    pair_data = [
        (1, "Alice", 65),     # ID 1 is Alice, weight 65kg
        (2, "Bob", 80),       # ID 2 is Bob, weight 80kg
        (3, "Charlie", 72.5)  # ID 3 is Charlie, weight 72.5kg
    ]

    # Pre-calculate and store pairs based on the sample data logic: 
    # Pair differences are calculated between specific individuals defined in a hypothetical list of relationships.
    
    # Define explicit relationships (ID_A, ID_B) with their weights from samples
    relationships = [
        ((1, 2), pair_data[0][2], pair_data[1][2]),   # Alice vs Bob: |65 - 80| = 15.0 kg difference
        ((3, 1), pair_data[2][2], pair_data[0][2]),   # Charlie vs Alice: |72.5 - 65| = 7.5 kg difference
    ]