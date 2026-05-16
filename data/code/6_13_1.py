def calculate_weight_difference(weight1, weight2):
    return abs(weight1 - weight2)
if __name__ == '__main__':
    try:
        weight1_str = "100"
        weight2_str = "150.5"
        weight1 = float(weight1_str)
        weight2 = float(weight2_str)
        difference = calculate_weight_difference(weight1, weight2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")