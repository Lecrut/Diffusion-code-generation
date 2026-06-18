import json
from typing import Dict, Tuple, Optional

class WeightPairManager:
    """
    A dictionary-based solution to store multiple weight pairs 
    and provide a function to quickly retrieve the difference between any two stored weights.
    
    Attributes:
        data (Dict[Tuple[int, int], float]): Internal storage mapping tuple of indices to their calculated differences.
    """

    def __init__(self):
        # Initialize an empty dictionary for storing pre-calculated differences based on index tuples
        self.data = {}

    def add_pair(self, weight1: int, weight2: int) -> None:
        """
        Adds a new pair of weights to the manager. The difference is calculated and stored 
        under a tuple key representing (index_of_weight1, index_of_weight2).
        
        Args:
            weight1 (int): First weight value.
            weight2 (int): Second weight value.
            
        Note: This method assumes unique weights or handles duplicates by overwriting if the same pair exists.
        """
        # Create a canonical key for the pair to ensure uniqueness regardless of order
        sorted_pair = tuple(sorted((weight1, weight2)))
        
        self.data[sorted_pair] = abs(weight1 - weight2)

if __name__ == '__main__':
    pass
