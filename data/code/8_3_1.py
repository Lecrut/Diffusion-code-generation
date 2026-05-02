import sys
def calculate_area(length, width):
    try:
        area = float(length) * float(width)
        return area
    except ValueError:
        return None
if __name__ == '__main__':
    input_data = ["10", "5"]
    if len(input_data) >= 2:
        length = input_data[0]
        width = input_data[1]
        result = calculate_area(length, width)
        if result is not None:
            print(result)
        else:
            print("Error: Invalid input provided.")
    else:
        print("Error: Insufficient input provided.")