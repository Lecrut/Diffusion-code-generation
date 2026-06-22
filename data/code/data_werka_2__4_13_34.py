def miles_to_feet(miles):
    return miles * 5280

def feet_to_miles(feet):
    return feet / 5280

if __name__ == '__main__':
    sample_miles = 1.5
    sample_feet = 7920
    
    converted_feet = miles_to_feet(sample_miles)
    converted_miles = feet_to_miles(sample_feet)
    
    print(f"{sample_miles} miles is equal to {converted_feet} feet")
    print(f"{sample_feet} feet is equal to {converted_miles} miles")