def convert_kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def convert_miles_to_kilometers(miles):
    return miles / 0.621371

def display_conversion(distance, unit):
    if unit == 'km':
        miles = convert_kilometers_to_miles(distance)
        print(f"{distance} kilometers is {miles:.4f} miles")
    elif unit == 'mi':
        kilometers = convert_miles_to_kilometers(distance)
        print(f"{distance} miles is {kilometers:.4f} kilometers")
    else:
        print("Invalid unit. Use 'km' or 'mi'.")

if __name__ == '__main__':
    display_conversion(5, 'km')
    display_conversion(10, 'mi')