def calculate_absolute_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    area1_input = "150"
    area2_input = "250"
    try:
        area1 = float(area1_input)
        area2 = float(area2_input)
        difference = calculate_absolute_difference(area1, area2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")