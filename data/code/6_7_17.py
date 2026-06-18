"""
Dictionary-based solution to store weight pairs and retrieve their differences efficiently.
This module does not use input(), sys.stdin, argparse required arguments, or any interactive prompts.
It includes a self-contained example block with hard-coded sample values that runs without user interaction.
"""

class WeightPairStorage:
    """A class designed to manage multiple (weight_a, weight_b) pairs and quickly compute their differences."""

    def __init__(self):
        # Initialize an empty dictionary where keys can be any hashable identifier 
        # for a pair, or we could store the difference directly indexed by unique identifiers.
        # Here, each entry maps a simple string key (e.g., "pair_0") to the actual weights tuple.
        self._pairs = {}

    def add_pair(self, key, weight_a: float, weight_b: float):
        """
        Adds a new pair of weights under the given key.
        
        Args:
            key (hashable): Unique identifier for this pair.
            weight_a (float): First weight in the pair.
            weight_b (float): Second weight in the pair.
        """
        self._pairs[key] = (weight_a, weight_b)

    def get_difference(self, key: str) -> float:
        """
        Retrieves and returns the absolute difference between two weights for a stored pair.
        
        Args:
            key (str): The unique identifier of the pair to look up.
            
        Returns:
            float: The absolute difference |weight_a - weight_b|, or None if not found.
            
        Raises:
            KeyError: If the provided key does not exist in the stored pairs.
        """
        if key not in self._pairs:
            raise KeyError(f"No pair data available for key '{key}'.")
        
        weights = self._pairs[key]
        return abs(weights[0] - weights[1])

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, network access, or file I/O is used here.

    storage = WeightPairStorage()

    # Sample Data Entry 1: Pair "alpha" with weights 50 and 30 kg
    storage.add_pair("alpha", 50, 30)

    # Sample Data Entry 2: Pair "beta" with weights 12.5 and 8.2 metric tons (treated as float)
    storage.add_pair("beta", 12.5, 8.2)

    # Sample Data Entry 3: Another pair to test retrieval reliability
    storage.add_pair("gamma", -40, -60)  # Negative weights for edge case testing on absolute diff logic

    print("--- Weight Pair Difference Report ---")

    try:
        diff_alpha = storage.get_difference("alpha")
        print(f"Difference for 'alpha': {diff_alpha} kg")

        diff_beta = storage.get_difference("beta")
        print(f"Difference for 'beta': {diff_beta}")

        # Testing the pair with negative numbers to ensure correct absolute difference calculation
        diff_gamma = storage.get_difference("gamma")
        print(f"Difference for 'gamma' (with negatives): |{-40 - (-60)}| -> Math: 20, Calc: {abs(-40 + 60)}")

    except KeyError as e:
        # This block handles the case where a non-existent key is queried. 
        # While not part of 'normal' operation in this sample run, it demonstrates error handling logic requested implicitly by "function to retrieve".
        print(f"Error occurred while retrieving pair '{e.args[0]}'")

    print("--- Operation Complete ---")