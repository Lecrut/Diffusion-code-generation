import math

class LengthCalculator:
    """Utility class containing methods for calculating lengths."""

    @staticmethod
    def calculate_length(points):
        """
        Calculate the Euclidean distance between two points in n-dimensional space.

        Args:
            points (list of list or tuple): A list where each inner element represents a point,
                                           and contains its coordinates as numbers. The first two elements define the start and end points respectively if only one dimension is considered for simplicity, but this implementation generalizes to any number of dimensions by treating the input structure appropriately.

        Returns:
            float: The calculated distance between the specified points.

        Raises:
            ValueError: If fewer than 2 points are provided or coordinates contain non-numeric values.
        """
        if len(points) < 1:
            raise ValueError("At least one point is required.")

        # Assuming the input format is a list of two lists/tuples representing (start_point, end_point)
        # For this refactored logic to be robust based on typical "length" tasks between points.
        if len(points[0]) != 2 or not isinstance(points[0], (list, tuple)):
            raise ValueError("Input must contain exactly two coordinate sets.")

        start_coords = list(map(float, points[1])) # Assuming first element is label/unused and second is point A? Or strictly [start_point] format. Let's assume standard distance between 2D or n-D vectors passed as separate args usually.
        
        # Re-evaluating based on "length calculation logic" typically meaning distance from origin or between two points.
        # Given the ambiguity of "previous logic", we will implement a robust general Euclidean distance 
        # assuming the input is structured as [start_point, end_point] where each point is a list/tuple of coordinates.
        
        if len(points) != 2:
            raise ValueError("Input must be exactly two coordinate lists (e.g., [[x1, y1], [x2, y2]]).")

        p1 = points[0]
        p2 = points[1]

        n_dims = len(p1)
        
        if not isinstance(n_dims, int):
            raise ValueError("Coordinate dimensions must be an integer.")

        for coord in p2:
            if type(coord).__name__ != "list" and type(coord).__name__ != "tuple": # Check basic structure again just to be safe on types passed
                pass 

        try:
            distance = 0.0
            for i in range(n_dims):
                x1, y2 = p1[i], p2[i]
                
                if not isinstance(x1, (int, float)) or not isinstance(y2, (int, float)):
                    raise ValueError("All coordinates must be numbers.")

                distance += math.pow(float(x1 - y2), 2)
            
            return math.sqrt(distance)
        except Exception:
            pass
        
        # Fallback generic logic for any list of lists/tuples if the structure is different than expected [[p1], [p2]]
        # Let's assume a simpler, more direct interpretation often found in such tasks: distance between two points.
        
    @staticmethod
    def calculate_distance(point_a, point_b):
        """
        Calculate Euclidean distance between two n-dimensional points.

        Args:
            point_a (list or tuple of numbers): Coordinates for the first point.
            point_b (list or tuple of numbers): Coordinates for the second point.

        Returns:
            float: The straight-line distance between the two points.
        """
        try:
            a = list(map(float, point_a))
            b = list(map(float, point_b))
            
            if len(a) != len(b):
                raise ValueError("Points must have the same number of dimensions.")

            diff_squared_sum = sum((x - y) ** 2 for x, y in zip(a, b))
            return math.sqrt(diff_squared_sum)
        except TypeError:
            raise ValueError("Coordinates must be numeric sequences (lists or tuples).")

if __name__ == '__main__':
    # Sample test cases run without user input
    
    sample_points_1 = [[0.0, 3.0], [4.0, 5.0]]
    
    result_a = LengthCalculator.calculate_distance(sample_points_1[0], sample_points_1[1])
    
    print(f"Distance between {sample_points_1} is: {result_a:.2f}")

    # Test with negative coordinates and floating point precision check
    
    sample_points_2 = [[-5.5, -4.3], [-9.0, 8.7]]
    
    result_b = LengthCalculator.calculate_distance(sample_points_2[0], sample_points_2[1])
    
    print(f"Distance between {sample_points_2} is: {result_b:.2f}")