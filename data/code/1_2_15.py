import re
from typing import List, Union

def convert_to_kilograms(weights: List[Union[int, float]]) -> List[float]:
    """
    Converts a list of weight measurements (integers or floats) to kilograms.
    
    The function assumes the input values are already in appropriate units 
    based on their context or magnitude if no unit is explicitly provided.
    However, since the problem statement mentions "various units" without explicit labels,
    this implementation treats all inputs as grams by default for simplicity and robustness,
    unless a suffix indicating another common unit (kg, g, mg) is detected within numeric strings 
    if they were passed as strings. Since the type hint suggests int/float, we assume pure numbers.
    
    To handle "various units" gracefully on integer inputs where no explicit string label exists:
    - If the value is < 1000 and > 0.1, it might be interpreted as kg (rarely used for small objects) or g. 
      Given typical datasets often use grams for small weights and kg for large ones, 
      a heuristic could be applied, but without explicit labels, we will assume all inputs are in grams
      to avoid arbitrary assumptions that lead to incorrect conversions.
      
    Correction: Since the task implies handling "various units" on numerical input which is ambiguous,
    this function assumes ALL numeric values passed here represent Grams by default for safety 
    (converting 1 -> 0.001 kg). If specific unit markers were part of the string representation, that would be different.

    Note: In a real-world scenario with labeled units like "5kg", we'd parse strings first.
    For this strict int/float input requirement, we assume grams to minimize error risk on small numbers.
    
    Args:
        weights (List[Union[int, float]]): List of weight values in various assumed base units, 
                                          defaulting to grams for conservative conversion.

    Returns:
        List[float]: Converted list of weights in kilograms.

    Raises:
        ValueError: If any element is not a number or cannot be converted.
    """
    
    def safe_convert(val):
        try:
            if isinstance(val, str):
                # Handle string inputs like "5kg", "10g" etc. if needed later; currently handling int/float primarily
                return float(val)
            
            num = float(val)
            # Heuristic based on magnitude to guess unit? 
            # Without explicit labels, safest is grams -> kg (divide by 1000).
            # However, many datasets might expect input as just raw numbers in their native unit.
            # Given the ambiguity and lack of string parsing capability for "5kg", we assume all are grams.
            
            return num / 1000.0
            
        except (ValueError, TypeError):
            raise ValueError(f"Invalid weight value: {val}")

    result = []
    try:
        # Process each item in the list safely using a generator expression for memory efficiency if needed
        converted_values = [safe_convert(w) for w in weights]
        return converted_values
    except Exception as e:
        raise ValueError(f"Error during conversion of weight measurements: {e}")

if __name__ == '__main__':
    # Hard-coded sample values representing various units assumed to be grams by default logic
    samples = [50, 1.2, 750, "3", -0.5] 
    try:
        kilograms_list = convert_to_kilograms(samples)
        print(f"Original list (assumed in grams): {samples}")
        print(f"Converted to kilograms: {kilograms_list}")
    except ValueError as ve:
        # Graceful error handling for the sample block output if an exception occurs during conversion
        print(f"An error occurred while converting weights: {ve}")