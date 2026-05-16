import sys
def meters_to_feet(meters):
    return meters * 3.28084
if __name__ == '__main__':
    sample_meters = 10
    try:
        input_value = float(sample_meters)
        result = meters_to_feet(input_value)
        print(f"{sample_meters} meters is equal to {result:.2f} feet")
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")