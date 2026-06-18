"""
Module: WeightPairDictionaryManager

Provides a dictionary-based solution to store multiple weight pairs 
and retrieve their difference efficiently.

Usage Example (hard-coded):
    >>> data = {
    ...     'pair1': {'weight_a': 50, 'weight_b': 30},
    ...     'pair2': {'weight_a': 80, 'weight_b': 40}
    ... }
    >>> get_difference('pair1')
    20.0

This module does not require user input, command-line arguments, 
network access, or pre-existing files to run the sample block.
"""

class WeightPairManager:
    """
    A manager class that stores weight pairs in a dictionary and provides
    methods to calculate differences between weights within each pair.
    
    Attributes:
        data (dict): Internal storage for weight pairs where keys are unique identifiers 
                     and values are dictionaries containing 'weight_a' and 'weight_b'.
    """

    def __init__(self, initial_data=None):
        """
        Initialize the WeightPairManager with optional pre-loaded data.
        
        Args:
            initial_data (dict, optional): Dictionary of weight pairs to populate on start.
                Expected format: {key: {'weight_a': float, 'weight_b': float}}
        """
        self.data = {}
        if initial_data is not None and isinstance(initial_data, dict):
            for key, pair in initial_data.items():
                # Ensure the structure matches expected format with error handling
                if isinstance(pair, dict) and all(k in pair for k in ('weight_a', 'weight_b')):
                    self.data[key] = {'weight_a': float(pair['weight_a']), 
                                      'weight_b': float(pair['weight_b'])}

    def add_pair(self, key, weight_a, weight_b):
        """
        Add a new weight pair to the dictionary.
        
        Args:
            key (str): Unique identifier for the pair.
            weight_a (float or int): First weight value.
            weight_b (float or int): Second weight value.
            
        Raises:
            ValueError: If any of the weights is not a number.
        """
        try:
            self.data[key] = {
                'weight_a': float(weight_a), 
                'weight_b': float(weight_b)
            }
        except (ValueError, TypeError):
            raise ValueError("Both weight values must be numeric.")

    def get_difference(self, key):
        """
        Retrieve the absolute difference between weights for a specific pair.
        
        Args:
            key (str): The unique identifier of the weight pair.
            
        Returns:
            float: Absolute difference |weight_a - weight_b|.
                
        Raises:
            KeyError: If the provided key does not exist in stored data.
        """
        if key not in self.data:
            raise KeyError(f"No such pair found with identifier '{key}'.")
        
        return abs(self.data[key]['weight_a'] - self.data[key]['weight_b'])

    def get_all_pairs_count(self):
        """
        Return the total number of stored weight pairs.
        
        Returns:
            int: Count of keys in the data dictionary.
        """
        return len(self.data)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files needed)
    
    # Sample Data Structure
    sample_pairs = {
        'apple_vs_orange': {'weight_a': 150.0, 'weight_b': 200.0},
        'red_ball_blue_ball': {'weight_a': 45.5, 'weight_b': 67.8},
        'box_small_box_large': {'weight_a': 30.0, 'weight_b': 100.0}
    }

    # Initialize manager with sample data
    weight_manager = WeightPairManager(initial_data=sample_pairs)

    print("Weight Pair Dictionary Manager - Sample Execution")
    print("-" * 45)
    
    # Test retrieval for specific pairs
    try:
        diff_apple_orange = weight_manager.get_difference('apple_vs_orange')
        print(f"Difference (Apple vs Orange): {diff_appole_orange:.2f}")

        diff_ball_pair = weight_manager.get_difference('red_ball_blue_ball')
        print(f"Difference (Red Ball vs Blue Ball): {diff_ball_pair:.2f}")
        
    except KeyError as e:
        # This block handles the case if a key is missing, though sample data covers these keys.
        pass

    # Demonstrate adding a new pair dynamically without external input
    try:
        weight_manager.add_pair('new_item', 50, 90)
        print(f"Added 'new_item' successfully.")
        
        diff_new = weight_manager.get_difference('new_item')
        print(f"Difference (New Item): {diff_new}")
    except Exception as e:
        # Silent catch for unexpected errors during add operation in isolated run
        pass

    # Verify count of pairs
    total_pairs = weight_manager.get_all_pairs_count()
    print("-" * 45)
    print(f"Total number of stored pairs: {total_pairs}")