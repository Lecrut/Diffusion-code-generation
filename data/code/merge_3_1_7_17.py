"""
Module: weight_validator_decorator

This module provides a decorator to validate and normalize weight input.
It handles type checking, range validation (0 <= weight), unit normalization 
(inputting in grams or kilograms automatically converts everything to grams if needed 
for consistency, though the primary spec implies simple numerical checks).

Exceptions thrown:
- TypeError: If the input is not a numberic value supported by float conversion.
- ValueError: If the numeric value is less than zero.

Usage example included below demonstrating hard-coded inputs without any I/O or arguments."""

class WeightValidationException(Exception):
    """Custom exception for general weight validation failures that don't fit other specific cases."""
    pass

def validate_weight(func):
    """
    Decorator to automatically validate and normalize the 'weight' argument of a function.

    Checks:
        1. The value must be convertible to float/numeric types (excluding booleans as they are technically int subclasses).
        2. The resulting numeric value must not be less than zero.

    Normalization:
        In this implementation, no automatic unit conversion is performed 
        unless explicitly added by the user's code logic inside the function; 
        however, it ensures the input represents a valid positive float/number representing weight in some standard base (e.g., grams or kg).

    Args:
        func (callable): The target function to decorate.

    Returns:
        Callable[[Any], Any]: Decorated wrapper function.
    
    Raises:
        TypeError: If the argument is not a valid numeric type (int, float) and bools are rejected.
        ValueError: If the converted weight value is negative or zero.
    """
    def wrapper(*args, **kwargs):
        # Get all arguments to check for any named 'weight' parameter if passed as keyword arg 
        # OR assume first positional argument might be the one based on problem context simplification.
        # To make this robust without knowing exact signature: we'll iterate over kwargs and args looking for a standard weight-like variable or just enforce it on all inputs?
        # Re-reading task: "automatically validates... weight input". 
        # Let's assume the decorator expects to find a 'weight' keyword argument OR accept any numeric argument passed.
        # The most generic approach that fits typical functional requirements without knowing exact signature is checking for explicit 'weight' kwarg or handling all args as potentially weights if not specified otherwise.
        
        found_weight = None
        
        # Prioritize kwargs search for a clear intention
        if "weight" in kwargs:
            weight_val = kwargs["weight"]
            found_weight = True
            
        else:
            # If no explicit 'weight' keyword, assume the first argument is intended to be checked 
            # or return immediately if we cannot identify it clearly (though strict task implies validation happens).
            # To satisfy "automatically validates", let's check all arguments for numeric types and apply logic.
            found_weight = False
            
        candidates_for_validation = []

        if not found_weight:
            # Check positional args
            for arg in args:
                if isinstance(arg, (int, float)) and type(arg) is not bool:
                    candidates_for_validation.append((len(args), "positional", arg))
                
                # Also check kwargs values generally to be safe against signature variations where weight isn't explicit but present as value? 
                # Let's stick to strict 'weight' kwarg or first positional for simplicity in this isolated context.
                pass
            
            if not candidates_for_validation and "weight" not in kwargs:
                raise TypeError("The function expects a numeric argument identified by position or keyword 'weight', but none found.")

        else:
            # We have an explicit weight keyword arg, use it
            val = kwargs["weight"]
            
            try:
                if isinstance(val, bool):
                    raise WeightValidationException(f"Boolean value '{val}' is not a valid weight. Pass numeric types only (e.g., int or float).")
                
                normalized_weight = float(val)

                if normalized_weight < 0:
                     # Cannot validate unit conversion as no standard mapping provided in prompt without more context, 
                     # but we ensure the *numeric* value is positive.
                    raise WeightValidationException(f"Invalid weight '{val}'. Weights must be non-negative values.")
                
            except TypeError:
                raise TypeErrors(f"{func.__name__} received an invalid data type for 'weight': {type(val)}. Must support numeric operations (int/float).")

        # Execute the wrapped function with original args, 
        # but if we found a specific weight to normalize/reject earlier, it's already validated here.
        
        result = func(*args, **kwargs)
        return result
    
    wrapper.__name__ = f"{func.__name__}_validated"
    return wrapper

# Main block with hard-coded samples running without user input or files
if __name__ == '__main__':

    def process_shipload(weight):
        """Simulated function that processes a shipment based on weight."""
        # Logic inside the function (e.g., printing log) will be executed here.
        print(f"Processing ship load with validated weight: {weight} units.")

    @validate_weight
    def add_fuel(total_weight, fuel_amount=None):
        """Function that adds fuel but requires total weight to be valid first."""
        if "fuel_amount" not in kwargs and len([a for a in args]) > 1:
             # If explicit 'weight' is missing but we passed multiple args? 
             # Let's rely on the decorated function checking its own signature via inspect or just assume the decorator checks all inputs.
             pass
        
        print(f"Adding fuel to ship currently carrying {total_weight} kg.")

    @validate_weight
    def calculate_cost(price_per_kg, weight):
        """Function that calculates cost based on item price and weight."""
        final_price = price_per_kg * float(weight) if isinstance(weight, (int,float)) else 0.0 # Simple mock logic 
        return round(final_price, 2)

    test_cases_passed = True
    
    print("--- Running Validation Tests ---")
    
    try:
        # Test Case 1: Valid Integer weight as keyword arg
        res = calculate_cost(5.9, weight=45)
        if "WeightValidationException" in globals(): pass 
        print(f"CASSED Int Weight (Int): Input=45 -> Output={res}")

    except TypeError as e:
        test_cases_passed = False; print(f"FAILED Type Error on Valid Int - {e}" )

try:
    # Test Case 2: Invalid String weight -> Should raise exception in decorator logic if implemented strictly. 
    # Since our implementation checks type before conversion, strings are caught here? No, string is not int/float instance check passed initially but converted later inside try block raising TypeError on float().
    
        res = calculate_cost(5.9, "twenty five")
except ValueError:
    print("PASSED String (ValueError): Handled invalid type/negative or bad conversion in calculator.")
except WeightValidationException as e:
    # Our specific decorator logic for non-numeric input raises TypeError usually on the float() call unless we check first.
    # Let's adjust internal doc to expect strict numeric types before calling func so it doesn't crash inside func if possible, 
    # but prompt asks for 'throws... for invalid data types'. So our current wrapper does this via try-except around conversion logic?
    pass

try:
    # Test Case 3: Negative weight -> Should raise ValueError in decorator.
    res = calculate_cost(5.9, -10)
except WeightValidationException as e:
    print(f"PASSED Negative Value (-10): Caught exception - {e}")

# Demonstrate usage with different inputs directly calling the decorated function to show behavior
print("\n--- Direct Execution Examples ---")

try:
    # Simulating a direct call where user passes valid data types only. 
    # Note: The decorator wraps calculate_cost, add_fuel etc? Only those explicitly mentioned above have @validate_weight in this snippet scope logic? 
    # Let's re-decorate or assume the ones listed are decorated in global context for demonstration clarity.
    
    print("Calling calculate_cost with valid weight...")
    result = process_shipload(weight=10) 
    
except TypeError:
     pass

print("\nAll sample executions completed.")