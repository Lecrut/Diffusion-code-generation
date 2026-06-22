import math

def calculate_diagonal(length, width):
    return math.sqrt(length ** 2 + width ** 2)

def calculate_radius(circumference):
    return circumference / (2 * math.pi)

if __name__ == '__main__':
    length = 3
    width = 4
    diagonal = calculate_diagonal(length, width)
    
    circumference = 10
    radius = calculate_radius(circumference)
    
    ratio = diagonal / radius
    print(ratio)