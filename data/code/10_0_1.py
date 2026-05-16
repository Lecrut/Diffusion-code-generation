import sys
def calculate_average(temp1, temp2):
    return (temp1 + temp2) / 2
if __name__ == '__main__':
    try:
        temp1_str = "25.5"
        temp2_str = "30.5"
        temp1 = float(temp1_str)
        temp2 = float(temp2_str)
        average = calculate_average(temp1, temp2)
        print(average)
    except ValueError:
        print("Error: Invalid input. Please ensure both inputs are valid numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")