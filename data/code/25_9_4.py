class DataProcessor:
    """A simple class demonstrating instance attribute checking."""

    def __init__(self, value):
        self.value = value

    @staticmethod
    def check_zero(instance_attr_name, obj_instance=None):
        """
        Checks if a specific instance attribute is equal to zero.

        Args:
            instance_attr_name (str): The name of the attribute to inspect.
            obj_instance: An optional object instance containing the attribute. 
                         If None, checks against 'self' within the calling class context.

        Returns:
            bool: True if the attribute is 0, False otherwise.
        """
        # Determine which instance's attribute to check
        target_obj = obj_instance if obj_instance else self
        
        try:
            attr_value = getattr(target_obj, instance_attr_name)
            return attr_value == 0
        except AttributeError:
            raise ValueError(f"Attribute '{instance_attr_name}' not found on the object.")

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed.

    # Create instances with various integer and float zero scenarios
    dp1 = DataProcessor(0)
    dp2 = DataProcessor(-5)
    dp3 = DataProcessor(None)  # Non-numeric value for demonstration
    
    print("Testing attribute 'value' across different instance states:")
    
    result_one = dp1.check_zero('value')
    print(f"Is dp1.value (0) equal to zero? {result_one}")

    result_two = dp2.check_zero('value', obj_instance=dp3)  # Check dp3's value (-5) via static method with explicit arg
    print(f"Does dp3 have 'value' == -5? Is it zero? {not result_two} (Expected: False)")

    try:
        result_three = dp1.check_zero('missing_attr')
        print("Error check failed.")
    except ValueError as e:
        print(f"Catch expected error for missing attribute: {e}")