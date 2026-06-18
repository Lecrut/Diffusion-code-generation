class NumberChecker:
    def compare_value(self, other):
        """
        Compares self.value with other.value.
        
        Args:
            other (NumberChecker): Another instance of NumberChecker to compare against.
            
        Returns:
            bool: True if self.value is greater than other.value, False otherwise.
        """
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or arguments)
    checker1 = NumberChecker()
    checker2 = NumberChecker()

    # Setting attributes directly since no constructor was specified in the task description,
    # but assuming standard object behavior where .value needs to be set.
    # We will simulate setting values for demonstration purposes within this block.
    
    # Example 1: self.value (50) > other.value (40) -> True
    checker1.value = 50
    checker2.value = 40
    
    result_1 = checker1.compare_value(checker2)

    # Example 2: self.value (30) > other.value (60) -> False
    checker1.value = 30
    checker2.value = 60
    
    result_2 = checker1.compare_value(checker2)

    print(f"Comparison 1 ({checker1.value} vs {checker2.value}): {result_1}")
    print(f"Comparison 2 ({checker1.value} vs {checker2.value}): {result_2}")