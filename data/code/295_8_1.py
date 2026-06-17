import sys
def convert_miles_to_km(miles):
    kilometers = miles * 1.60934
    return kilometers
if __name__ == '__main__':
    miles_to_convert = 100
    kilometers_result = convert_miles_to_km(miles_to_convert)
    print(f"{miles_to_convert} miles is equal to {kilometers_result} kilometers")