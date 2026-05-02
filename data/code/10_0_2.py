import sys
def calculate_average(temp1, temp2):
    if not isinstance(temp1, (int, float)) or not isinstance(temp2, (int, float)):
        raise TypeError("Both inputs must be numeric.")
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
        print("Error: One or both inputs could not be converted to a valid number.")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")