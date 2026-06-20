import math

def are_floats_close(val1, val2):
    return math.isclose(val1, val2)

if __name__ == '__main__':
    print(are_floats_close(5.0, 5.0))
    print(are_floats_close(3.14, 3.1400000000000004))
    print(are_floats_close(float('inf'), float('inf')))
    print(are_floats_close(float('-inf'), float('-inf')))
    print(are_floats_close(float('nan'), float('nan')))