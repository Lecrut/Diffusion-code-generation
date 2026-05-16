def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number")
    radius = diameter / 2
    area = 3.141592653589793 * (radius ** 2)
    return area
if __name__ == '__main__':
    try:
        diameter1 = 10
        area1 = calculate_circle_area(diameter1)
        print(f"The area of a circle with diameter {diameter1} is: {area1}")
        diameter2 = 0
        area2 = calculate_circle_area(diameter2)
        print(f"The area of a circle with diameter {diameter2} is: {area2}")
        diameter3 = -5
        area3 = calculate_circle_area(diameter3)
        print(f"The area of a circle with diameter {diameter3} is: {area3}")
    except ValueError as e:
        print(f"Error: {e}")