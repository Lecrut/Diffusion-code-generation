class ComparisonTool:
    def check_greater(self, value1, value2):
        """
        Compares two values using Python's native comparison operators.
        
        Args:
            value1 (any comparable type): The first value to compare.
            value2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if value1 is strictly greater than value2, False otherwise.
        """
        return value1 > value2

if __name__ == '__main__':
    tool = ComparisonTool()

    # Hard-coded sample values covering integers and floats for testing efficiency
    samples_int = (45, 30)
    samples_float = (3.14, 2.71)
    
    result_1 = tool.check_greater(*samples_int)
    print(f"Integer comparison ({samples_int[0]} > {samples_int[1]}): {result_1}")

    result_2 = tool.check_greater(*samples_float)
    print(f"Float comparison ({samples_float[0]} > {samples_float[1]}): {result_2}")