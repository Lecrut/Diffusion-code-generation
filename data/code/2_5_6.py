import math

def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    """
    Scales a given list of volume data by a specified multiplication factor,
    ensuring floating-point precision is maintained throughout the operation.

    Args:
        volumes (list[float]): The initial list of volume values to scale.
        factor (float): The multiplicative factor applied to each element.

    Returns:
        list[float]: A new list containing the scaled volume values.
    
    Raises:
        ValueError: If any input value is not a number or if inputs are invalid types.
    """
    # Validate and convert all elements in the volumes list to float for precision handling
    validated_volumes = []
    for vol in volumes:
        try:
            val = float(vol)
            validated_volumes.append(val)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid volume value '{vol}'. All elements must be numeric.")

    # Calculate scaled values with explicit floating-point arithmetic
    if not isinstance(factor, (int, float)) or math.isnan(float(factor)):
        raise ValueError("Factor must be a valid number.")
    
    factor = float(factor)
    
    return [v * factor for v in validated_volumes]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input
    initial_data = [10.5, 23.7, 42.9, -5.2, 0.0]
    
    try:
        scaled_result = scale_volumes(initial_data, factor=2)
        
        # Output the result in a clear format for verification
        print("Original volumes:", initial_data)
        print(f"Scaled by {factor}:")
        for idx, (orig, new_vol) in enumerate(zip(initial_data, scaled_result)):
            print(f"  [{idx}] {orig} * {factor} = {new_vol}")
        
    except ValueError as e:
        print(f"Error during calculation: {e}")