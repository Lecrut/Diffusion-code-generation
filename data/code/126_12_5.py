import math

def are_floats_close(a, b):
    return math.isclose(a, b)
if __name__ == '__main__':
    print(are_floats_close(0.1 + 0.2, 0.3))
    print(are_floats_close(float('nan'), float('nan')))
    print(are_floats_close(float('inf'), float('inf')))
    print(are_floats_close(float('-inf'), float('-inf')))
    print(are_floats_close(float('inf'), float('-inf')))