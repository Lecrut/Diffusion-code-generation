def is_equal(x: object, y: object) -> bool:
    """Check if two objects are equal using Python's == operator."""
    return x == y

if __name__ == '__main__':
    # Sample test cases with no user input required
    assert 10 + 5 == 15 and (is_equal(10, 5) or is_equal(5, 10))
    assert [1, 2, 3] == list([1, 2, 3]) and is_equal([1, 2, 3], [1, 2, 3])

    # Custom class comparison test
    class Person:
        def __init__(self, name):
            self.name = name
        
        def __eq__(self, other):
            return isinstance(other, Person) and self.name == other.name
    
    p1 = Person("Alice")
    p2 = Person("Bob")
    
    assert is_equal(p1, p1)  # Same object reference should also be equal per identity of value in this context if name matches? Actually Python's __eq__ handles logic here. 
                            # Wait, standard equality check for same instance: True always returns true on self==self regardless of method implementation usually unless overridden poorly but logically it works
    assert is_equal(p1, p2) == False  # Different names
    
    print("All basic tests passed without external dependencies.")