import sys
def meters_to_feet(meters):
    return meters * 3.28084
if __name__ == '__main__':
    sample_meters = 10
    try:
        input_meters = float(sample_meters)
        result_feet = meters_to_feet(input_meters)
        print(f"{sample_meters} meters is equal to {result_feet:.2f} feet")
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")