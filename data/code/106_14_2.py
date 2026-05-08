import sys
if __name__ == '__main__':
    try:
        year1_str = "2023"
        year2_str = "2021"
        year1 = int(year1_str)
        year2 = int(year2_str)
        difference = abs(year1 - year2)
        print(f"Year 1: {year1}")
        print(f"Year 2: {year2}")
        print(f"The absolute difference is: {difference}")
    except ValueError:
        print("Error: Please enter valid integer years.")