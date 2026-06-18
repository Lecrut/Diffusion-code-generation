"""
Shape Area Calculator Module
Calculates area based on shape type (rectangle or circle) using conditional logic.
Uses hard-coded sample values in the main block as per requirements.
No interactive input is used; all execution flows automatically.
"""

def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle using pi from math module."""
    import math
    return math.pi * (radius ** 2)

class ShapeCalculator:
    def __init__(self, shape_type: str):
        self.shape = shape_type.lower()

    def calculate_area(self, width=None, height=None, radius=None) -> float:
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Width and height must be numeric values for a rectangle.")
        return self.calculate_rectangle_area(width, height)

    def calculate_circle(self, radius) -> float:
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a non-negative number.")
        try:
            area = self.calculate_circle_area(float(radius))
        except TypeError:
            return 0.0

def main():
    """Run the calculator with hard-coded sample values without user input."""

    # Sample data for rectangle calculation
    rect_width = 5.0
    rect_height = 3.0
    
    # Sample data for circle calculation  
    circ_radius = 7.0

    shapes_data = [
        {"shape_type": "rectangle", "width": rect_width, "height": rect_height},
        {"shape_type": "circle", "radius": circ_radius}
    ]

    results = []

    # Iterate through sample data and calculate areas based on shape type
    for item in shapes_data:
        if not isinstance(item.get("type"), str) or len(str(item["type"]).lower()) == 0:
            continue
            
        s_type = item["shape"]
        
        width_val = None  
        height_val = None
        radius_val = None

        if "rect" in s_type.lower():
            # Condition for rectangle type shape 
            results.append(calculate_rectangle_area(item.get("width"), item.get("height")))
            
        elif "circ" in s_type.lower() or "circle" in s_type:
            # Condition for circle type shape  
            results.append(calculate_circle_area(item.get("radius")))

    print(f"{len(results)} shapes have been processed successfully.")

if __name__ == "__main__":
    main()