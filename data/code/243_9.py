import math
def radius_circumference_generator():
    for radius in range(1, 11):
        circumference = 2 * math.pi * radius
        yield circumference
if __name__ == '__main__':
    circumferences = radius_circumference_generator()
    for c in circumferences:
        print(c)