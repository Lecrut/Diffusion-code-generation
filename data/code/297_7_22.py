def cubic_meters_to_gallons(cubic_meters):
    conversion_factor = 264.172
    return cubic_meters * conversion_factor

if __name__ == '__main__':
    sample_cubics = [3, 5]
    for cubics in sample_cubics:
        gallons = cubic_meters_to_gallons(cubics)
        print(f"{cubics} cubic meters is equal to {gallons:.2f} gallons")