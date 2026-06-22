EDGE = 4.0

def compute_cube_volume(length):
    if length <= 0:
        raise ValueError("Length must be positive")
    return length * length * length

if __name__ == '__main__':
    v = compute_cube_volume(EDGE)
    print(v)