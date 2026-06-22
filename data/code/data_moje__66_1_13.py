KILOMETER_TO_METER = 1000

def convert_kilometers_to_meters(kilometers: float) -> float:
    return kilometers * KILOMETER_TO_METER

if __name__ == '__main__':
    kilometers_value = 5.0
    meters_value = convert_kilometers_to_meters(kilometers_value)
    print(meters_value)