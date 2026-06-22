FEET_PER_YARD = 0.3333333333333333
INCHES_PER_FOOT = 12

def convert_length(feet_value, inches_per_foot=12):
    return feet_value * inches_per_foot

if __name__ == '__main__':
    sample_feet = 6
    conversion_factor = INCHES_PER_FOOT
    calculated_inches = convert_length(sample_feet, conversion_factor)
    print(calculated_inches)