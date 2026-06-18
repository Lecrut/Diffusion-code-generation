class Comparator:
    @staticmethod
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects using the built-in equality operator (==).
        
        Args:
            self: Reference to the class instance (required for method signature consistency).
            a: First object to compare.
            b: Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Sample test cases without user input or external dependencies
    
    class Person:
        def __init__(self, name):
            self.name = name
        
        def __eq__(self, other):
            if isinstance(other, Person):
                return self.name == other.name
            return False

    obj1_person = Person("Alice")
    obj2_person = Person("Bob")
    
    # Test 1: Different objects with same content (if implementing custom __eq__)
    result_custom_eq = Comparator.check_equality(None, Person("Charlie"), Person("Charlie"))
    
    # Test 2: Built-in equality for simple types using the provided method via class variable access if needed
    # However, since check_equality is a staticmethod in this design but requires 'self', 
    # we will instantiate to demonstrate usage as per standard OOP patterns where self might be expected.
    
    # Re-defining slightly to accept 'cls' or allow calling without instantiation if preferred by user needs?
    # The task asks for check_equality(self, a, b). Let's stick strictly to the signature but make it static-like 
    # by passing None as first arg logic inside or just letting Python handle non-binding.
    
    # Actually, standard practice with 'self' in method even if static is:
    class Comparator2:
        def check_equality(self, a, b):
            return self.__class__.check_equality_static(a, b)

    @classmethod
    def check_equality_static(cls, a, b):
        return a == b
    
    # To strictly follow the prompt "method within a class named Comparator that contains method check_equality(self, a, b)":
    pass 

# Refined implementation to ensure exact signature compliance while being runnable:

class Comparator:
    @staticmethod
    def _check(a, b):
        return a == b
    
    # The prompt specifically asks for `check_equality(self, a, b)`. 
    # If we make it staticmethod but the signature is (self, a, b), 'self' will be None.
    # We can implement logic inside that handles both class methods and instance calling if needed,
    # or simply ignore self since it's not used for data access in this context of pure equality check.

class Comparator:
    
    def check_equality(self, a, b):
        """Compares two objects using the == operator."""
        return a == b

if __name__ == '__main__':
    # Sample values to test functionality
    
    class CustomClass:
        def __init__(self, val):
            self.val = val
        
        def __eq__(self, other):
            if not isinstance(other, CustomClass):
                return NotImplemented
            return self.val == other.val

    c1 = CustomClass(10)
    c2 = CustomClass(10)
    
    # Test instance method access (passing None as 'self' is fine for static-like behavior logic here 
    # but strictly, if called on an object: obj.c.check_equality(obj_c1, obj_c2))
    
    comp_obj = Comparator()
    
    # Call with arbitrary objects passed via the specific signature
    res_int = comp_obj.check_equality(50, 50)
    res_str = comp_obj.check_equality("Hello", "World")
    res_custom_same = comp_obj.check_equality(c1, c2)
    res_custom_diff = comp_obj.check_equality(c1, CustomClass(9))

    assert res_int == True, "Integers should be equal"
    assert res_str == False, "Strings should not be equal"
    # Note: Since we didn't define __eq__ in the example run above for simplicity of 'a==b', 
    # Python uses default object identity (not same instance), so c1 != c2.
    # If you want custom logic results here, you must implement __eq__. 
    
    print(f"50 == 50: {res_int}")       # True
    print(f"'Hello' == 'World': {res_str}")   # False  
    print(f"c1 (val=10) == c2 (val=10): {res_custom_same}") # False by default Python object identity unless __eq__ implemented
    
    # To demonstrate custom equality effectively with the provided method:
    
    class BetterCustomClass:
        def __init__(self, val):
            self.val = val
        
        def __eq__(self, other):
            return isinstance(other, BetterCustomClass) and self.val == other.val

    bc1 = BetterCustomClass(42)
    bc2 = BetterCustomClass(42)
    
    res_better = comp_obj.check_equality(bc1, bc2)
    print(f"bc1 (val=42) == bc2 (val=42): {res_better}") # True
    
    assert res_better == True