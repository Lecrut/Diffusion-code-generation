import math

class WeightValidationException(Exception):
    """Base exception for weight validation errors."""
    pass

class InvalidDataTypeError(WeightValidationException):
    """Raised when input is not a valid numeric type (int or float)."""
    pass

class ImpossibleValueError(WeightValidationException):
    """Raised when the provided value is physically impossible (<= 0)."""
    pass

def validate_weight(func):
    """Decorator that validates and normalizes weight inputs.

    Validates:
        - Input must be int or float.
        - Value must be strictly positive (> 0).
    
    Normalization:
        - Converts floats to integers if they are whole numbers (e.g., 5.0 -> 5).
        - Rounds other valid decimals up to the nearest integer for consistency 
          in this specific design, though typically weight might need rounding rules.
          Here we round half-up to ensure minimal representation error is handled gracefully.

    Throws:
        InvalidDataTypeError if input type is not numeric.
        ImpossibleValueError if value <= 0.
    
    Args:
        func (callable): The function to decorate.
        
    Returns:
        callable: A wrapped version of the original function with validation logic.
    """

    def wrapper(*args, **kwargs):
        # Extract weight argument; assume it's the first positional arg based on common patterns
        if not args or len(args) == 0:
            raise WeightValidationException("No weight provided.")
        
        raw_weight = args[0]

        try:
            numeric_value = float(raw_weight)
            
            # Check for impossible values (must be > 0)
            if numeric_value <= 0:
                raise ImpossibleValueError(f"Weight must be positive, got {raw_weight}.")
                
            # Normalize to integer if it's a whole number
            normalized_int = int(round(numeric_value))
            
        except TypeError as e:
            raise InvalidDataTypeError(
                f"Invalid data type for weight. Expected numeric (int/float), "
                f"got {type(raw_weight).__name__}."
            ) from e

        # Re-raise impossible value errors if they occurred during conversion logic implicitly handled above, 
        # but explicitly check again after rounding to be safe against edge cases like -0.1 becoming 0
        if normalized_int <= 0:
             raise ImpossibleValueError(f"Normalized weight {normalized_int} is not positive.")

        args = (normalized_int,) + args[1:]
        
        return func(*args, **kwargs)

    return wrapper

@validate_weight
def calculate_mass(weight):
    """Calculates mass based on a normalized weight."""
    # Example logic: Mass = Weight * 2.0 kg/unit
    return f"Mass calculated for {weight} unit(s): {weight * 2.0:.1f} kg."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("Valid integer", 5),
        ("Valid float (whole)", 10.0),
        ("Valid float (decimal)", 23.7),
        ("Invalid string", "ten"),
        ("Impossible zero", 0),
        ("Impossible negative", -5),
    ]

    print("Running weight validation tests...\n")

    for description, value in test_cases:
        try:
            result = calculate_mass(value)
            status = f"SUCCESS -> {result}"
        except InvalidDataTypeError as e:
            status = f"ERROR (Invalid Data Type): {e}"
        except ImpossibleValueError as e:
            status = f"ERROR (Impossible Value): {e}"

        print(f"{description} ({value!r}):")
        print(status)
        print("-" * 40)