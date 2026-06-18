class TemperatureComparator:
    def compare(self, temp1, temp2):
        """
        Compares two temperatures and prints a descriptive string indicating their relationship.
        
        Args:
            temp1 (float or int): First temperature value.
            temp2 (float or int): Second temperature value.
            
        Returns:
            None: Prints the comparison result directly.
        """
        if isinstance(temp1, str) and '°' in temp1[0]:
            # Handle potential non-numeric string inputs by extracting numbers if needed, 
            # but for this strict requirement we assume valid numeric input based on task description.
            pass

        try:
            num1 = float(temp1)
            num2 = float(temp2)
            
            if abs(num1 - num2) < 1e-6:
                print(f"{temp1} is equal to {temp2}")
            elif temp1 > temp2:
                diff = round(temp1 - temp2, 2)
                print(f"{temp1} is higher than {temp2} by {diff} degrees")
            else:
                diff = round(num2 - num1, 2)
                print(f"{temp1} is lower than {temp2} by {diff} degrees")

        except (ValueError, TypeError):
            # Fallback if input types are unexpected strings but not numbers, 
            # though the task implies valid numeric comparison context.
            try:
                temp1 = float(temp1)
                temp2 = float(temp2)
            except ValueError:
                print(f"Could not convert inputs to comparable values.")

if __name__ == '__main__':
    comp = TemperatureComparator()
    
    # Hard-coded sample values for testing various comparison scenarios
    samples = [
        (10, 35),       # Positive difference
        (-40.5, -20),   # Negative numbers with positive diff
        (65, 65.00001)  # Near equality check
    ]

    for t1, t2 in samples:
        comp.compare(t1, t2)
    
    # Additional explicit test case to ensure robustness logic is hit clearly
    print("\n--- Explicit Single Case ---")
    result_msg = "Equal" if abs(30.5 - 30.5) < 1e-6 else ("Higher", "Lower")[1] + f" by {round(abs(30.5 - (30.5+2)), 2)}" # Simulate logic manually for clear output
    comp.compare(30.5, 30.5)