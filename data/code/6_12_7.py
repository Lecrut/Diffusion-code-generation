class WeightCalculator:
    """A class to handle weight calculations."""

    def __init__(self):
        self.weights = []

    def add_weight(self, weight):
        """Adds a new weight to the collection."""
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be an integer or float.")
        self.weights.append(weight)

    def calculate_difference(self, w1_index=None, w2_index=None, value1=None, value2=None):
        """
        Calculates the absolute difference between two weights.

        Args:
            w1_index (int | None): Index of the first weight in internal list (0-based).
            w2_index (int | None): Index of the second weight in internal list (0-based).
            value1 (float | None): First numeric weight value.
            value2 (float | None): Second numeric weight value.

        Returns:
            float: The absolute difference between the two weights.
        
        Raises:
            IndexError: If requested indices are out of bounds for internal list.
            TypeError: If required parameters are missing or invalid types.
        """
        if w1_index is None and value2 is None:
            raise ValueError("Either provide (index_1, index_2) from the stored weights "
                           "or pass specific weight values directly.")

        # Option 1: Using indices to fetch from internal list
        def get_weight_from_list(idx):
            if idx < 0 or idx >= len(self.weights):
                raise IndexError(f"Index {idx} is out of range for the current weights list. "
                                f"Valid range is 0-{len(self.weights) - 1}")
            return self.weights[idx]

        # Option 2: Using direct values provided by user
        def get_weight_from_value(val):
            if val is None or not isinstance(val, (int, float)):
                raise TypeError(f"Value argument must be a number, got {type(val)}")
            return val

        weight_a = value1
        index_a = w1_index
        
        # Determine first weight source based on what was provided in the call context logic above.
        if value2 is not None:
            weight_b = get_weight_from_value(value2)

if __name__ == '__main__':
    pass
