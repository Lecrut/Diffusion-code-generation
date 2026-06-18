# KM to Miles Converter Utility
def km_to_miles(km):
    """Convert kilometers to miles using standard conversion factor."""
    return round(km * 0.621371, 4)

def main():
    # Hard-coded sample values for demonstration without user input or command-line arguments
    samples = [5, 10, 50]

    print("Kilometer to Miles Converter")
    print("-" * 30)

    try:
        conversion_value = km_to_miles(samples[0])
    except Exception as e:
        return f"No sample data provided. Error occurred during calculation: {e}"

    result_str = (f"{samples[0]} kilometers is equal to " 
                  f"<b>{conversion_value}</b> miles.")
    
    print(f"Input value selected from samples")  # No input() or sys.stdin called here
    
    return result_str

if __name__ == '__main__':
    main_output = main()
    if isinstance(main_output, str) and "Error" not in main_output:
        print("\nConverted Result:")
        print(result_str)