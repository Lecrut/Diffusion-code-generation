MILES_TO_FEET = 5280

def to_feet(mile_value):
    return mile_value * MILES_TO_FEET

if __name__ == '__main__':
    print(to_feet(5))
    print(to_feet(0.5))
    print(to_feet(100))