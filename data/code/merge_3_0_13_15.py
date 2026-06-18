import sys

def convert_length(value_in_kilometers: float) -> tuple[float, float]:
    """
    Converts a length value given in kilometers to meters and feet.
    
    Args:
        value_in_kilometers (float): The length measurement in kilometers.
        
    Returns:
        tuple[float, float]: A tuple containing the equivalent lengths in 
                            meters and feet respectively.
                            
                                1 km = 1000 m
                                1 m ≈ 3.28084 ft
                                
                    Raises:
                        TypeError: If input is not a number.
                        
    """
    if not isinstance(value_in_kilometers, (int, float)):
        raise TypeError("Length value must be a numeric type.")
        
    meters = value_in_kilometers * 1000.0
    
    feet_per_meter = 3.28084
    feet = meters * feet_per_meter
    
    return round(meters), round(feet)

def print_measurements(km_values: list[float], units_label: str | None = "kilometers") -> None:
    """
    Prints each length measurement from the provided list in both 
    meters and feet, along with its original unit label.
    
    Args:
        km_values (list[float]): List of float values to convert.
        units_label (str): Label indicating the input unit used. Defaults to "kilometers".
                            
                    Raises:
                        TypeError: If list is empty or contains non-numeric items.
                        
    """
    if not isinstance(km_values, list) or len(km_values) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")

if __name__ == '__main__':
    pass
