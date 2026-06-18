class ValueChecker:
    def __ne__(self, other):
        """Check if two provided values are unequal."""
        return self != other

def main():
    checker = ValueChecker()
    
    # Hard-coded sample values to demonstrate the functionality without user input
    value_a = 10
    value_b = 20
    
    result_unequal = (value_a != value_b)
    print(f"Are {value_a} and {value_b} unequal? {result_unequal}")

    
    # Additional test cases with different types
    num_val = 42.5
    text_val = "hello"
    bool_val = True
    
    result_num_text = (num_val != text_val)
    print(f"Impartial comparison between number and string: {result_num_text}")

if __name__ == '__main__':
    main()