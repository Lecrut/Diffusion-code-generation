def calculate_perimeter(a, b):
    h = ((a - b) ** 2) / ((a + b) ** 2)
    return (a + b) * (1 + (3 * h) / (10 + (4 - 3 * h) ** 0.5))

if __name__ == '__main__':
    ellipse1 = (3, 4)
    perimeter1 = calculate_perimeter(*ellipse1)
    print(f"Perimeter for {ellipse1}: {perimeter1}")
    
    ellipse2 = (10, 20)
    perimeter2 = calculate_perimeter(*ellipse2)
    print(f"Perimeter for {ellipse2}: {perimeter2}")
    
    ellipse3 = (1, 1)
    perimeter3 = calculate_perimeter(*ellipse3)
    print(f"Perimeter for {ellipse3}: {perimeter3}")