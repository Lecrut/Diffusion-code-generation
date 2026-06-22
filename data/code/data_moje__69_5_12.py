import numpy as np

def convert_miles_to_feet(miles):
    feet = np.array(miles, dtype=np.float64) * 5280.0
    return feet

if __name__ == '__main__':
    sample_miles = [1.0, 2.5, 10.0]
    result = convert_miles_to_feet(sample_miles)
    print(result)