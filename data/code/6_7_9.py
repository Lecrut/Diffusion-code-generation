import json
from typing import Dict, Tuple, Optional

class WeightPairManager:
    """
    A dictionary-based solution to store multiple weight pairs 
    and provide a function to quickly retrieve the difference for any stored pair.
    
    Attributes:
        data (Dict[Tuple[int, int], float]): Internal storage mapping tuple of weights to their difference.
    """

    def __init__(self):
        self.data = {}  # Key is a tuple of two integers representing weight pairs; Value is the calculated difference.

    def add_pair(self, w1: int, w2: int) -> None:
        """
        Adds or updates a weight pair in the dictionary.
        
        Args:
            w1 (int): First weight value.
            w2 (int): Second weight value.
            
        Note: The difference is calculated as abs(w1 - w2). If the same tuple exists, it will be updated.
        """
        key = (w1, w2)
        self.data[key] = abs(w1 - w2)

    def get_difference(self, w1: int, w2: int) -> Optional[float]:
        """
        Retrieves the pre-calculated difference for a stored weight pair.
        
        Args:
            w1 (int): First weight value.
            w2 (int): Second weight value.
            
        Returns:
            float or None: The absolute difference if found, otherwise None.
        """
        key = (w1, w2)
        return self.data.get(key)

def main():
    # Hard-coded sample values to demonstrate functionality without user input
    
    manager = WeightPairManager()

    # Adding initial pairs
    manager.add_pair(50, 30)   # Difference: 20
    manager.add_pair(100, 75)  # Difference: 25
    manager.add_pair(45, 45)   # Difference: 0

    # Simulating retrieval operations with hard-coded queries
    
    retrieved_1 = manager.get_difference(50, 30)
    retrieved_2 = manager.get_difference(100, 75)
    
    print(f"Difference for (50, 30): {retrieved_1}") # Expected: 20.0
    
    if retrieved_2 is None:
        print("Pair not found.")
    else:
        print(f"Difference for (100, 75): {retrieved_2}") # Expected: 25.0

    
if __name__ == '__main__':
    main()