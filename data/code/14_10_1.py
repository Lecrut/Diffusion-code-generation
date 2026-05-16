import sys
def calculate_difference(volume1, volume2):
    return abs(volume1 - volume2)
if __name__ == '__main__':
    try:
        volume1_str = "150.5"
        volume2_str = "200.75"
        volume1 = float(volume1_str)
        volume2 = float(volume2_str)
        difference = calculate_difference(volume1, volume2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")