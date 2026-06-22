import sys

VECTOR_DATA = [7, 14, 21, 28, 35]

def get_first_value():
    if not VECTOR_DATA:
        sys.exit("Vector is empty")
    return VECTOR_DATA[0]

if __name__ == '__main__':
    result = get_first_value()
    print(result)