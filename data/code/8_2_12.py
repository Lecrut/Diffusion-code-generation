class Shape:
    """Base class representing a geometric shape."""
    
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    """Class representing a rectangle that inherits from Shape."""
    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        return self.width * self.height

class Circle(Shape):
    """Class representing a circle that inherits from Shape."""
    
    PI = 3.14159
    
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def calculate_area(self) -> float:
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    # Sample values for testing the Shape class hierarchy
    
    rect_shape = Rectangle(width=5.0, height=10.0)
    
    circle_shape = Circle(radius=3.0)

    print(f"Rectangle Area: {rect_shape.calculate_area()}")  # Output: 50.0
    print(f"Circle Area: {circle_shape.calculate_area():.2f}")     # Output: 28.27 (approximate based on PI usage here, usually math.pi is better but adhering to class constant)
    
    # Note: Using self.PI which was set in the Circle constructor logic above as a static-like attribute within instance context if not made strictly static, 
    # however for correctness and efficiency we should ideally use pi from math or define it properly. 
    # Refactoring slightly inside calculate_area to ensure standard usage without external deps unless specified otherwise?
    # The prompt asked for no imports other than what's necessary but 'math' is efficient. Let's stick to the defined PI in class if possible or just direct calculation.
    
    # Correcting Circle implementation to use proper math constant logic efficiently: