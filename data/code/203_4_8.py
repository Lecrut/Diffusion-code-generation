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
    print(f"Comparing {complex1} and {complex2}: Result is {result1}")
    complex3 = (-1, 0)
    complex4 = (0, -1)
    result2 = compare_magnitude(complex3, complex4)
    print(f"Comparing {complex3} and {complex4}: Result is {result2}")
    complex5 = (1, 1)
    complex6 = (2, 0)
    result3 = compare_magnitude(complex5, complex6)
    print(f"Comparing {complex5} and {complex6}: Result is {result3}")