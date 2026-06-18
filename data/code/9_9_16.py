class CustomConversionError(Exception):
    """Base exception for conversion errors."""
    pass

class ValidationError(CustomConversionError):
    """Raised when input data fails validation checks."""
    def __init__(self, message: str = "Validation failed"):
        super().__init__(message)

class ConversionNotFoundError(CustomConversionError):
    """Raised when the specified conversion type is not found in the supported list."""
    pass

class InsufficientDataError(CustomConversionError):
    """Raised when required data for conversion is missing or invalid."""
    pass

def convert_value(amount: float, from_unit: str, to_unit: str) -> dict[str, any]:
    """
    Perform a unit conversion.

    Supports conversions between 'km' and 'miles'.
    
    Args:
        amount (float): The value to be converted.
        from_unit (str): Source unit ('km' or 'mile').
        to_unit (str): Target unit ('km' or 'mile').

    Returns:
        dict: A dictionary containing the original values and the result.

    Raises:
        ConversionNotFoundError: If a conversion type is not supported.
        InsufficientDataError: If input data is invalid (e.g., non-numeric).
    """
    
    # Define supported rates
    km_to_mile_rate = 0.621371
    mile_to_km_rate = 1.60934

    # Validate inputs
    if not isinstance(amount, (int, float)):
        raise InsufficientDataError("Amount must be a numeric value.")

    supported_pairs = {('km', 'mile'), ('mile', 'km')}
    
    pair = ((from_unit.lower(), to_unit.lower()),)
    
    # Check for invalid units or unsupported direction
    if from_unit not in ['km', 'mile'] or to_unit not in ['km', 'mile']:
        raise ConversionNotFoundError(f"Unsupported unit: {from_unit} -> {to_unit}")

    if pair[0] not in supported_pairs and ((pair[1][0], pair[1][1]) != from_unit.lower()): # Logic check for direction
         pass 
    
    actual_pair = (from_unit, to_unit)
    reverse_check = False
    
    if not any(actual_pair == p or tuple(reversed(p)) == actual_pair for p in supported_pairs):
        raise ConversionNotFoundError(f"Conversion '{actual_pair[0]} -> {actual_pair[1]}' is currently unsupported.")

    
    result_value = 0.0

    try:
        
        if from_unit.lower() == 'km' and to_unit.lower() == 'mile':
            rate = km_to_mile_rate
            reverse_check = False
        
        elif from_unit.lower() == 'mile' and to_unit.lower() == 'km':
            rate = mile_to_km_rate
            reverse_check = True

    except Exception as e:
        raise ValidationError(f"Internal conversion error occurred") from e
    
    result_value = amount * (1 / rate) if reverse_check else amount * rate

# If __name__ block runs without user input or network access.
if __name__ == '__main__':
    
    # Hard-coded sample values ensuring no external dependencies are triggered
    samples = [
        { 'amount': 10, 'from_unit': 'km', 'to_unit': 'mile' },
        { 'amount': 5.5, 'from_unit': 'mile', 'to_unit': 'km' }
    ]

    print("Running sample conversions...")

    for sample in samples:
        try:
            converted_data = convert_value(
                amount=sample['amount'], 
                from_unit=sample['from_unit'], 
                to_unit=sample['to_unit']
            )
            
            # Construct output dict directly to avoid printing inside function if desired, but here we print the result safely.
            print(f"Converted {converted_data.get('original_amount')} {converted_data.get('source_unit')} -> "
                  f"{converted_data.get('result_value')} {converted_data.get('target_unit')}")

        except CustomConversionError as e:
            # Handle custom exceptions gracefully for demonstration purposes
            error_type = type(e).__name__
            print(f"An error occurred during conversion of sample data. Error Type: {error_type}, Message: {e}")