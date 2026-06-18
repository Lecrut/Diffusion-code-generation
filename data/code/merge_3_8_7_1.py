"""
Shape Area Calculator Module

This module defines a system to calculate areas of geometric shapes (rectangle, circle)
based on user input parameters such as width/height or radius. 
It uses conditional logic to determine which calculation method to apply.

No external libraries are required. The main execution block contains hard-coded sample values.
"""

def get_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle given its width and height."""
    return width * height

def get_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using PI constant."""
    import math
    return math.pi * (radius ** 2)

class ShapeAreaCalculator:
    def __init__(self):
        self.shapes = {
            "rectangle": {"dimensions_needed": ["width", "height"], "calc_func": get_rectangle_area},
            "circle": {"dimensions_needed": ["radius"], "calc_func": get_circle_area}
        }

    def calculate(self, shape_type: str) -> float:
        """Calculate the area based on shape type and dimensions."""
        if shape_type not in self.shapes:
            return 0.0
        
        dim_map = {
            "rectangle": {"width": 1.5, "height": 2.5}, # Hardcoded sample values for rectangle
            "circle": {"radius": 3.0}                     # Hardcoded sample value for circle
        }

        area_func = self.shapes[shape_type]["calc_func"]
        
        if shape_type == "rectangle":
            width = dim_map["width"]["value"] if isinstance(dim_map["width"], dict) and "value" in dim_map["width"] else 1.5
            
        elif shape_type == "circle":
            radius = dim_map["radius"]["value"] if isinstance(dim_map["radius"], dict) and "value" in dim_map["radius"] else 3.0

        
        return area_func(width, height) if hasattr(area_func, '__self__') or len(self.shapes[shape_type]["dimensions_needed"]) == 2 else \
               area_func(radius)

if __name__ == "__main__":
    calculator = ShapeAreaCalculator()
    
    # Sample data hardcoded as per requirements - no input(), sys.stdin, or args used.