conversion_factors = {
    "nm": 1.852
}

def convert_nautical_miles_to_kilometers(nautical_miles):
    if not isinstance(nautical_miles, (int, float)):
        raise TypeError("Input value must be numeric.")
    
    kilometers = nautical_miles * conversion_factors["nm"]
    return round(kilometers, 2)

if __name__ == '__main__':
    sample_value = 10
    result = convert_nautical_miles_to_kilometers(sample_value)
    print(result)