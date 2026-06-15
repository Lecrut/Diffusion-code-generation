import math
def compare_magnitude(c1, c2):
    mag1 = math.sqrt(c1[0]**2 + c1[1]**2)
    mag2 = math.sqrt(c2[0]**2 + c2[1]**2)
    if mag1 > mag2:
        return c1
    elif mag2 > mag1:
        return c2
    else:
        return c1
if __name__ == '__main__':
    complex1 = (3, 4)
    complex2 = (5, 12)
    result1 = compare_magnitude(complex1, complex2)
    print(f"Complex 1: {complex1}")
    print(f"Complex 2: {complex2}")
    print(f"Result: {result1}")
    complex3 = (1, 1)
    complex4 = (-5, 0)
    result2 = compare_magnitude(complex3, complex4)
    print(f"Complex 3: {complex3}")
    print(f"Complex 4: {complex4}")
    print(f"Result: {result2}")
    complex5 = (0, 10)
    complex6 = (1, 1)
    result3 = compare_magnitude(complex5, complex6)
    print(f"Complex 5: {complex5}")
    print(f"Complex 6: {complex6}")
    print(f"Result: {result3}")