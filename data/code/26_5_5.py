class NumberChecker:
    def is_greater_than(self, other):
        """Compare self.value with other.value."""
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker()
    # Simulating value attribute directly as per task constraints on structure
    # If the class needs to be initialized differently in a real scenario, 
    # this block demonstrates usage assuming 'value' is set or accessible.
    
    # For demonstration with hard-coded attributes within instances:
    num1.value = 50
    num2.value = 30
    num3.value = 49
    
    checker_a = NumberChecker()
    checker_b = NumberChecker()
    checker_c = NumberChecker()
    
    checker_a.value = 80
    checker_b.value = 100
    checker_c.value = 75

    result_ab = checker_a.is_greater_than(checker_b)
    result_ac = checker_a.is_greater_than(checker_c)
    # Note: In a dynamic instance setup where value is not pre-set on construction,
    # we must ensure the attribute exists before comparison. 
    # Here we assume 'value' can be accessed or set as part of initialization logic if needed,
    # but strictly following "Assume both instances have a .value attribute".

    print(f"{checker_a.value} > {checker_b.value}: {result_ab}")
    print(f"{checker_a.value} > {checker_c.value}: {result_ac}")