class NumberTracker:
    def __init__(self, value):
        """Initialize the tracker with a starting value."""
        self.value = value

    def is_zero(self) -> bool:
        """Check if the instance attribute 'value' equals zero.

        Returns:
            bool: True if self.value == 0, False otherwise.
        """
        return self.value == 0

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    tracker_one = NumberTracker(5)
    tracker_two = NumberTracker(0)
    tracker_three = NumberTracker(-1)

    print(f"Is 5 equal to zero? {tracker_one.is_zero()}")   # False
    print(f"Is 0 equal to zero? {tracker_two.is_zero()}") # True
    print(f"Is -1 equal to zero? {tracker_three.is_zero()}") # False