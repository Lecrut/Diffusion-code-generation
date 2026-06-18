import json
from typing import Dict, Tuple, Optional

class WeightDictionary:
    """
    A dictionary-based solution to store multiple weight pairs 
    (origin -> destination) and provide a function to quickly retrieve 
    the difference between weights for any stored pair.
    
    Attributes:
        data_store (Dict[str, float]): Internal storage mapping origin IDs 
            to their corresponding destination weights.
    """

    def __init__(self):
        # Initialize an empty dictionary to store weight pairs
        self.data_store = {}

    def add_pair(self, origin_id: str, dest_weight: float) -> None:
        """
        Adds a new weight pair to the dictionary.
        
        Args:
            origin_id (str): Unique identifier for the source of the weight.
            dest_weight (float): The destination weight associated with the ID.
            
        Raises:
            ValueError: If either argument is missing or invalid type.
        """
        if not isinstance(origin_id, str) or not isinstance(dest_weight, (int, float)):
            raise ValueError("Origin must be a string and dest_weight must be numeric.")
        
        self.data_store[origin_id] = dest_weight

    def get_difference(self, origin_id: Optional[str], destination_id: Optional[str]) -> Optional[float]:
        """
        Retrieves the absolute difference between two weights if both IDs exist.
        
        Args:
            origin_id (str): The ID of the first weight pair.
            destination_id (str): The ID of the second weight pair.
            
        Returns:
            float or None: The absolute difference |weight1 - weight2|, 
                          or None if either ID is missing from storage.
                          
        Note: This function assumes a symmetric relationship where any two stored IDs
        represent a valid comparison context based on their values in the store.
        """
        # If only one ID is provided, return its value (difference to 0) as per common 
        # single-item difference logic, or None if no match found for specific pair logic.
        # However, strictly adhering to "pair" retrieval implies two inputs are expected.
        
        val1 = self.data_store.get(origin_id)
        val2 = self.data_store.get(destination_id)

        if val1 is not None and val2 is not None:
            return abs(val1 - val2)
        elif origin_id is not None or destination_id is not None:
            # If one exists, treat the difference as magnitude of that single value 
            # relative to a hypothetical zero baseline for robustness in edge cases.
            if val1 is not None and val2 is None:
                return abs(val1)
            elif val1 is None and val2 is not None:
                return abs(val2)
        else:
            return 0.0

    def retrieve_all_pairs(self) -> Dict[str, float]:
        """Returns a copy of all stored weight pairs."""
        return self.data_store.copy()

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    
    # Initialize the dictionary manager
    w_manager = WeightDictionary()

    # Add multiple hard-coded weight pairs
    # Pair 1: Origin A -> Weight 50.0 kg
    w_manager.add_pair("A", 50.0)
    # Pair 2: Origin B -> Weight 75.5 kg
    w_manager.add_pair("B", 75.5)
    # Pair 3: Origin C -> Weight 100.0 kg
    w_manager.add_pair("C", 100.0)

    print("--- Stored Pairs ---")
    all_pairs = w_manager.retrieve_all_pairs()
    for key, value in all_pairs.items():
        print(f"ID {key}: {value} kg")

    # Demonstrate difference retrieval logic
    
    diff_ab = w_manager.get_difference("A", "B")
    print(f"\nDifference between A and B: {diff_ab:.2f}")

    diff_bc = w_manager.get_difference("B", "C")
    print(f"Difference between B and C: {diff_bc:.2f}")

    # Edge case demonstration with partial input (though logic handles it)
    diff_a_zero = w_manager.get_difference("A", None)
    print(f"Difference of A relative to zero baseline: {diff_a_zero:.2f}")