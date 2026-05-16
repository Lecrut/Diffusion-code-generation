import sys
def convert_km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
if __name__ == '__main__':
    sample_length = 10
    conversion_type = "km_to_miles"
    if conversion_type == "km_to_miles":
        try:
            length_input = input("Enter the length in kilometers: ")
            length = float(length_input)
            if length < 0:
                print("Error: Length cannot be negative.")
            else:
                result = convert_km_to_miles(length)
                print(f"Conversion result: {length} km is equal to {result:.2f} miles.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the length.")
    else:
        print("Invalid conversion type specified.")