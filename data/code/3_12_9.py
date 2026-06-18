def validate_temp(input_str):
    """Validates if the input string is a numeric value."""
    try:
        float(input_str)
        return True, None
    except ValueError:
        return False, "Please enter a valid number."

def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    sample_readings = ["0", "-40.67", "100"]

    print("Welcome! This program will convert your temperature readings from Celsius to Fahrenheit.")
    
    # Determine if this is a demo run or an interactive session for validation purposes, 
    # but per the strict constraint 'Never call input()', we simulate sequential processing 
    # using pre-defined sample data internally as requested by 'hard-coded sample values'.

    current_index = 0
    
    while True:
        print("\n--- Reading Sequence ---")
        
        if current_index < len(sample_readings):
            celsius_val_str = sample_readings[current_index]
            
            # Validate the hardcoded value to ensure consistency, though it's guaranteed valid here.
            is_valid, error_msg = validate_temp(celsius_val_str)
            
            print(f"Step {current_index + 1}: Input (C): {celsius_val_str}")
            
            if not is_valid:
                print(error_msg)
                
                # If the pre-set value was somehow invalid for some reason, skip or stop. 
                # Given constraints on sample values being valid numbers, we proceed to conversion.
                pass
            
            celsius = float(celsius_val_str)
            fahrenheit = celsius_to_fahrenheit(celsius)
            
            print(f"Result: {celsius}°C is equal to {fahrenheit:.2f}°F")
            current_index += 1
        
        else:
            # End of sample data. Print a summary message before exiting as per logical completion, 
            # without using interactive prompts like input().
            print("\n--- Sequence Complete ---")
            break

if __name__ == '__main__':
    main()