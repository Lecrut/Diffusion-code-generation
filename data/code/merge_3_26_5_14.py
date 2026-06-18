class NumberChecker:
    def is_greater_than(self, other):
        """
        Compares this instance's value with another NumberChecker instance's value.
        
        Args:
            other (NumberChecker): The instance to compare against.
            
        Returns:
            bool: True if self.value > other.value, False otherwise.
        """
        return self.value > other.value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    checker_a = NumberChecker()
    checker_b = NumberChecker()

    # Assigning arbitrary integer values to the .value attribute as per assumption
    checker_a.value = 10
    checker_b.value = 5
    
    result = checker_a.is_greater_than(checker_b)
    
    print(f"{checker_a.value} > {checker_b.value}: {result}")

    # Additional test case where self is not greater than other
    checker_c = NumberChecker()
    checker_d = NumberChecker()
    checker_c.value = 3
    checker_d.value = 7
    
    result2 = checker_c.is_greater_than(checker_d)
    
    print(f"{checker_c.value} > {checker_d.value}: {result2}")