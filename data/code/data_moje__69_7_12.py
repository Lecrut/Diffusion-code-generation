def convert_miles_to_feet(miles_sequence):
    for mile in miles_sequence:
        yield mile * 5280

if __name__ == '__main__':
    distances = (1, 5, 10, 100, 1000)
    generator = convert_miles_to_feet(distances)
    for value in generator:
        print(value)