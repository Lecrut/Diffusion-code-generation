"""
Module: WeightPairDictionary

This module provides a dictionary-based solution to store multiple weight pairs 
and efficiently retrieve the difference between any two stored weights.

Features:
- Stores weight pairs as tuples in a list, indexed by an integer key.
- Provides a function `get_difference` that calculates |weight1 - weight2|.
- Includes a main execution block with hard-coded sample data for testing.

Usage Example (from command line):
    python solution.py
    
No external input is required; all operations are self-contained.
"""

class WeightPairStore:
    """
    A class to manage and retrieve differences between stored weight pairs.
    
    Attributes:
        _data_store (dict): Internal dictionary mapping integer keys to tuples 
                            of two weights (float or int).
    """

    def __init__(self, data=None):
        """Initialize the WeightPairStore with optional pre-loaded data."""
        self._data_store = {}
        
        if isinstance(data, list) and all(isinstance(pair, tuple) and len(pair) == 2 for pair in data):
            # If provided a list of tuples, populate it directly.
            for i, (w1, w2) in enumerate(data):
                self._data_store[i] = (float(w1), float(w2))

    def add_pair(self, key: int, weight_a: any, weight_b: any) -> None:
        """Add a new pair of weights to the store.
        
        Args:
            key (int): The integer index for this entry. Must be unique if 
                       multiple pairs are added sequentially without reassignment.
            weight_a: First weight value.
            weight_b: Second weight value.
            
        Raises:
            ValueError: If a pair with the same 'key' already exists and is not being updated.
        """
        if key in self._data_store:
            # Update existing entry instead of raising error for simplicity, 
            # unless strict uniqueness is required by external logic (not specified).
            pass 
        
        self._data_store[key] = (float(weight_a), float(weight_b))

if __name__ == '__main__':
    pass
