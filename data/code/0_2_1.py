import sys
def convert_km_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles
if __name__ == '__main__':
    sample_length = 10
    conversion_type = "km_to_miles"
    if conversion_type == "km_to_miles":
        try:
            input_length = int(sample_length)
            if input_length >= 0:
                result = convert_km_to_miles(input_length)
                print(f"Input Length: {input_length} km")
                print(f"Conversion: {input_length} km is equal to {result:.2f} miles")
            else:
                print("Error: Length cannot be negative.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer for the length.")
    else:
        print("Error: Invalid conversion type specified.")