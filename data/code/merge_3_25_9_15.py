class Counter:
    def __init__(self, initial_value=0):
        """Initialize a counter instance."""
        self.value = initial_value
    
    @property
    def is_zero(self) -> bool:
        """Check if the internal value attribute equals zero.
        
        Returns:
            bool: True if self.value == 0, False otherwise.
        """
        return self.value == 0

if __name__ == '__main__':
    # Sample values for testing without user input or file access
    sample_instances = [Counter(5), Counter(0)]

    print("Testing is_zero property:")
    for inst in sample_instances:
        result = inst.is_zero
        status = "Zero" if result else "Not Zero"
        print(f"Instance with value {inst.value}: {status}")