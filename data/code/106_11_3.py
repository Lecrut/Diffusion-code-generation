if __name__ == '__main__':
    year1 = 2023
    year2 = 1998
    try:
        y1 = int(year1)
        y2 = int(year2)
        difference = abs(y1 - y2)
        print(difference)
    except ValueError:
        print("Error: Invalid input. Please enter integers.")