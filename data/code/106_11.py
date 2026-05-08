def calculate_difference(year1, year2):
    return abs(year1 - year2)
if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    try:
        y1 = int(year1)
        y2 = int(year2)
        difference = calculate_difference(y1, y2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter integer values.")