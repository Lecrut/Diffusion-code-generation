class TemperatureComparator:
    """A class to compare two temperature values."""

    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.

        Args:
            temp1 (float or int): The first temperature value.
            temp2 (float or int): The second temperature value.

        Returns:
            None: Prints the comparison result directly.
        """
        if temp1 == temp2:
            print(f"{temp1} is equal to {temp2}.")
        elif temp1 > temp2:
            print(f"{temp1} is greater than {temp2}.")
        else:
            print(f"{temp1} is less than {temp2}.")

if __name__ == '__main__':
    # Hard-coded sample values for testing the TemperatureComparator class.
    comparator = TemperatureComparator()

    test_cases = [
        (30, 30),      # Equal case
        (45, 20),      # Greater than case
        (-10, 5),      # Less than case
        (float('inf'), float('-inf')), # Infinity cases for robustness check
    ]

    print("Running TemperatureComparator tests...\n")
    for t1, t2 in test_cases:
        comparator.compare(t1, t2)
        print()