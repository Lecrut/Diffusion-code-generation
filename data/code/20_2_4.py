class Comparator:
    @staticmethod
    def check_equality(a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            a: First object to compare.
            b: Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Integer equality
    result_int = Comparator.check_equality(5, 5)
    
    # Test 2: String equality
    result_str = Comparator.check_equality("hello", "world")
    
    # Test 3: List of integers (order matters in lists)
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result_list_diff = Comparator.check_equality(list_a, list_b)
    
    # Test 4: Custom class instance equality based on __eq__ if defined
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person(name={self.name}, age={self.age})"

    p1 = Person("Alice", 30)
    p2 = Person("Bob", 30)
    
    # Test custom object equality (should be False unless __eq__ is defined in subclass or uses default identity-like behavior for different instances, 
    # but here we test the basic comparison logic which defaults to type and id check for most built-in types without explicit __eq__)
    result_custom = Comparator.check_equality(p1, p2)

    print(f"Integer equality (5 == 5): {result_int}")          # True or False depending on implementation details if overridden elsewhere? No, integers are values. Wait: int comparison is value based. Corrected thought process below for final code generation to ensure clarity.
    
    # Re-evaluating integer logic above in mind: 
    # In Python 5 == 5 returns True. My previous mental note was slightly confused about 'value' vs identity, but the operator handles this correctly automatically.

    print(f"String equality ('hello' == 'world'): {result_str}")          # False
    print(f"List inequality ([1,2,3] != [4,5,6]): {not result_list_diff}")  # True (meaning lists are not equal) -> Output should reflect they are NOT equal? 
    # Let's fix the variable name meaning in output to be direct.

    # Corrected logic for final print:
    
    int_comp = Comparator.check_equality(5, 5)      # Expected: True
    str_comp = Comparator.check_equality("hello", "world")   # Expected: False
    
    custom_eq = Comparator.check_equality(p1, p2) # Default object equality checks type and id usually? Actually default __eq__ for built-in types is identity only if not overridden. Wait, Person has no __eq__, so it defaults to comparing instance attributes via dict comparison in Python 3? No, without __eq__, it compares the objects themselves which are distinct instances of different classes or same class but different ids unless specific logic exists.
    # Actually, for user-defined classes without __eq__ defined:
    # p1 == p2 checks if they are exactly equal by checking all attributes and values? 
    # NO. Without __eq__, it falls back to `object.__eq__` which is identity check (True only if same object). 
    # Wait, let me double check Python docs mentally.
    # "If the type of an instance does not define a comparison method... use == as equality test." -> Identity? No.
    # If no __eq__, it uses `is` logic essentially for most cases or raises TypeError if types differ significantly without implementation? 
    # Actually, default object.__eq__ returns True only if self is b (identity). 
    # So p1 == p2 should be False because they are different instances.
    
    print(f"Integer equality: {int_comp}")           # Expected: True
    print(f"String inequality ('hello' != 'world'): {str_comp}")  # Expected: False
    
    print(f"Custom object (p1 vs p2, no __eq__): {custom_eq} (Expected: False as they are different instances)")