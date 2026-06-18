class NumberChecker:
    def compare_greater(self, other):
        """Compares self.value with other.value."""
        return self.value > other.value

if __name__ == '__main__':
    num1 = NumberChecker()
    num2 = NumberChecker()
    
    # Set hard-coded sample values (assuming a way to set value if not provided by constructor)
    # Since the task implies we can use attributes, let's add a simple setter for demonstration 
    # or assume __init__ sets default. To make it runnable without changing class structure too much:
    
    try:
        num1.value = 100
        num2.value = 50
        
        result1 = num1.compare_greater(num2)
        print(f"NumChecker({num1.value}) > NumChecker({num2.value}): {result1}")
        
        # Test the reverse case for completeness in one block
        temp_val_3 = NumberChecker()
        temp_val_3.value = 75
        
        result2 = num2.compare_greater(temp_val_3)
        print(f"NumChecker({num2.value}) > NumChecker({temp_val_3.value}): {result2}")

    except AttributeError:
        # Fallback if value property doesn't exist initially and we can't easily modify class without external change
        pass