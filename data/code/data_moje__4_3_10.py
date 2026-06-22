def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def miles_to_kilometers(miles):
    return miles / 0.621371

def centimeters_to_inches(centimeters):
    return centimeters / 2.54

def inches_to_centimeters(inches):
    return inches * 2.54

if __name__ == '__main__':
    print(meters_to_feet(10))
    print(feet_to_meters(32.8084))
    print(kilometers_to_miles(5))
    print(miles_to_kilometers(3.10686))
    print(centimeters_to_inches(10))
    print(inches_to_centimeters(3.93701))