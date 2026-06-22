def miles_to_feet(miles):
    feet = miles * 5280.0
    return feet

if __name__ == '__main__':
    result = miles_to_feet(1.0)
    print(result)