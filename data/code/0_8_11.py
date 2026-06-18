def convert_to_miles(km: float) -> str:
    """Convert kilometers to miles."""
    return f"{km / 1.60934:.2f}"

def convert_to_kilometers(mile_value: float) -> str:
    """Convert a given mile value back to kilometers for consistency, 
    as the input was originally treated as length in a generic unit but required output in both."""
    # Since Python's round function can sometimes cause floating-point representation issues when displayed with f-string formatting,
    # we calculate directly using constants. 1 km = 0.621371 miles.
    return f"{mile_value / 0.621371:.2f}"

if __name__ == '__main__':
    # Sample values are hardcoded as requested, no interactive input used here for this block.
    sample_lengths = [50, 284.4]

    print("Converting kilometers to miles and kilometers:")
    print(f"Input: {sample_lengths[0]} km -> Miles: {convert_to_miles(sample_lengths[0])}, Kilometers: {convert_to_kilometers(1)}") # Note: The second output is just 1km since input was KM
    
    # Re-evaluating the task requirement based on ambiguity.
    # "prompts user to enter a length" implies an input type, but sample block says NO interactive input.
    # Usually this means 'Enter your name' -> loop() vs hardcode inputs for demo.
    # Let's assume the function is generic enough or we just use the hardcoded values in print logic 
    # which effectively demonstrates the conversion without actual user prompt interaction at runtime (except perhaps a dummy one if needed, but task says no interactive).
    
    # To strictly follow "continuously prompts" via code structure while satisfying sample block:
    # I will write the program to loop indefinitely, waiting for input.
    # However, since 'Do not use interactive input in the sample block', 
    # the main execution block will simulate a few iterations using hardcoded strings representing inputs.