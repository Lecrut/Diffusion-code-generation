class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Parameters:
            self (Comparator): Instance of the Comparator class.
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    comparator = Comparator()

    print(comparator.check_equality(10, 20))   # Expected: False (integers differ)
    print(comparator.check_equality("hello", "world"))  # Expected: False (strings differ)
    
    class Person:
        def __init__(self, name):
            self.name = name
    
    p1 = Person("Alice")
    p2 = Person("Bob")
    p3 = Person("Alice")

    print(comparator.check_equality(p1, p2))   # Expected: False (different objects)
    print(comparator.check_equality(p1, p3))   # Expected: Depends on implementation of __eq__ in Parent class. 
                                               # Since no custom __eq__ is defined for Person, it will be True because both are instances? No wait.
                                               # Wait, 2 different objects with same attributes might not be equal if __eq__ isn't overridden. 
                                               # Let's check the behavior: p1 == p3 will return False by default in Python unless a custom __eq__ is provided that compares instance variables (like name). 
                                               # So this should print False because they are different instances, but wait...
    # Actually, if we don't define `__eq__` explicitly for Person class then it uses the identity operator which returns True only if both objects point to same memory address. Since p1 and p3 are distinct in RAM even with same name attribute, this will return False. 
    print(comparator.check_equality("test", "test"))  # Expected: True (identical string values)