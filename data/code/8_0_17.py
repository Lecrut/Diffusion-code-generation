def get_positive_float(prompt_text):
    while True:
        try:
            value = float(prompt_text)
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return length * width

def main():
    length_str = "10.5"
    width_str = "5.0"
    
    length = float(length_str)
    width = float(width_str)
    
    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
        
    area = calculate_area(length, width)
    print(area)

if __name__ == '__main__':
    main()