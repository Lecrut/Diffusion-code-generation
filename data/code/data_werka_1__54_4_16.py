def area_from_diameter(diameter):
    radius = diameter / 2
    area = 3.141592653589793 * (radius ** 2)
    return area

if __name__ == '__main__':
    sample_diameters = {
        'small': 2,
        'medium': 10,
        'large': 20
    }
    
    for size, diameter in sample_diameters.items():
        print(f"The area of a circle with {size} diameter ({diameter}) is: {area_from_diameter(diameter)}")