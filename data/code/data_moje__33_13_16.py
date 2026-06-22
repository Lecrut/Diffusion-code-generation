TRIANGLE_BASE = 10
TRIANGLE_HEIGHT = 5

def triangle_area(base, height):
    if base <= 0 or height <= 0:
        return 0
    return base * height * 0.5

if __name__ == '__main__':
    print(triangle_area(TRIANGLE_BASE, TRIANGLE_HEIGHT))