import math
def calculate_circumference(radius):
    pi = 3.141592653589793                                                                                             
    circumference = 2 * radius * pi
    return circumference
if __name__ == '__main__':
    radius_value = 5.0
    circumference_result = 2 * radius_value * math.pi
    print(circumference_result)