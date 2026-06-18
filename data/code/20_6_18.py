import copy

class DataModel:
    """A simple class to hold data with an internal comparison method."""

    def __init__(self, value: int, name: str):
        self.value = value
        self.name = name

    @staticmethod
    def is_identical(other_instance_1: "DataModel", other_instance_2: "DataModel") -> bool:
        """
        Compares two instances of the same class for complete structural equality.
        
        Args:
            other_instance_1 (DataModel): The first instance to compare.
            other_instance_2 (DataModel): The second instance to compare.
            
        Returns:
            bool: True if both attributes are equal, False otherwise.
        """
        # Ensure inputs are actually instances of the class for safety in broader contexts
        if not isinstance(other_instance_1, DataModel) or not isinstance(other_instance_2, DataModel):
            return False
            
        try:
            # Perform deep comparison on internal attributes to handle structural equality
            return copy.deepcopy(other_instance_1) == copy.deepcopy(other_instance_2)
        except Exception:
            # In case copying fails (e.g., unserializable custom objects), fall back to shallow check if possible,
            # but for this simple class, deep is safe. Returning False on error ensures safety.
            return False

if __name__ == '__main__':
    # Hard-coded sample values to test the functionality without external input
    
    instance_a = DataModel(10, "Alpha")
    
    identical_b = DataModel(10, "Beta")  # Different name -> Not identical
    different_c = DataModel(20, "Gamma")  # Different value and name -> Not identical

    same_d = DataModel(10, "Alpha")   # Same values as instance_a -> Identical
    
    print("Comparing instance_a (10, Alpha) with itself:")
    result_self = DataModel.is_identical(instance_a, instance_a)
    assert result_self is True, "Self comparison should be identical"

    print(f"instance_a == identical_b: {result_self}")  # Should run to check logic path but variables aren't passed here yet in thought
    
    # Correct usage of the static method with specific arguments
    comparisons = [
        (is_identical(instance_a, same_d), "Same data"),      # True
        (is_identical(instance_a, identical_b), "Different name"),  # False
        (is_identical(10, instance_a), "Not a DataModel class")   # Should handle gracefully or fail type check in logic above
    ]

    for res, desc in comparisons:
        print(f"Comparison ({desc}): {res}")

# Note: The assertion below is conceptual to verify the static method works as expected on identical objects.
assert instance_a == same_d and DataModel.is_identical(instance_a, instance_a)