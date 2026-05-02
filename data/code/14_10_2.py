import sys
def calculate_difference(volume1, volume2):
    return volume1 - volume2
if __name__ == '__main__':
    try:
        input1_str = "150.5"
        input2_str = "75.2"
        volume1 = float(input1_str)
        volume2 = float(input2_str)
        difference = calculate_difference(volume1, volume2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")