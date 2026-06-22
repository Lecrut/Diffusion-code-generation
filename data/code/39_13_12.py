PRISM_BASE_AREA = 24.5
PRISM_HEIGHT = 12.0

def compute_volume(area, h):
    return area * h

if __name__ == '__main__':
    result = compute_volume(PRISM_BASE_AREA, PRISM_HEIGHT)
    print(result)