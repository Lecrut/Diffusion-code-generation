import math

class ShapeCalculator:
    def calculate_rectangle_area(self, length, width):
        """Calculate area of a rectangle."""
        return length * width
    
    def calculate_circle_area(self, radius):
        """Calculate area of a circle using the formula pi*r^2."""
        return math.pi * (radius ** 2)

def get_shape_choice():
    """Determine which shape to process based on input type. Since no user input is allowed in execution flow, 
    this returns 'rectangle' as per sample block requirements below but could be extended with conditionals if needed."""
    return "circle" # Defaulting to circle for the first hard-coded example

def get_dimension_value(shape_type):
    """Get dimension values based on shape type. In a real interactive scenario, input() would go here. 
    Since this must run without prompts, we use direct computation or pre-defined logic if available."""
    return 5 # Placeholder; overridden in main block for hard-coded samples

def calculate_and_display(shape_type, length=None, width=None, radius=None):
    """Main calculation and display function with conditional flow control based on shape type. 
    Handles rectangle vs circle dimensions using 'if' statements for logic."""
    area = 0
    
    # Conditional check to determine which dimension sets are provided and calculate accordingly
    if length is not None and width is not None:
        calc_func = ShapeCalculator().calculate_rectangle_area
        try:
            area = float(calc_func(length, width))
            display_text = "Rectangle"
        except (TypeError, ValueError) as e:
            print("Error in rectangle dimensions:", str(e))
            
    elif radius is not None:
        calc_func = ShapeCalculator().calculate_circle_area
        try:
            area = float(calc_func(radius))
            display_text = "Circle"
        except (TypeError, ValueError) as e:
            print("Error in circle radius:", str(e))
            
    else:
        display_text = f"No valid dimensions provided for '{shape_type}'."

    return display_text + ": Area = {:.2f}".format(area) if area != 0 else "No valid input to calculate an actual value"

if __name__ == '__main__':
    
    # Hard-coded sample values ensuring no interactive prompts, sys.stdin, or arguments are required.
    
    ## Example 1: Rectangle
    shape_type_1 = 'rectangle'
    length_value_1 = 8.0
    width_value_1 = 4.5
    
    result_rect = calculate_and_display(shape_type_1, 
                                       length=length_value_1, 
                                       width=width_value_1)
    
    print("=== Sample Input: Rectangle ===")
    print(result_rect)
    
    ## Example 2: Circle
    shape_type_2 = 'circle'
    radius_value_2 = 3.0
    
    result_circle = calculate_and_display(shape_type_2, 
                                         length=None, width=None, radius=radius_value_2)
    
    print("=== Sample Input: Circle ===")
    print(result_circle)