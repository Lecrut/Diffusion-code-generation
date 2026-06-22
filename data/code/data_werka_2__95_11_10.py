MIN_THRESHOLD = 0
MAX_THRESHOLD = 100
EVEN_DIVISOR = 2

def is_valid_triplet(x, y, z):
    bounds = (MIN_THRESHOLD, MAX_THRESHOLD)
    for value in (x, y, z):
        if value <= bounds[0]:
            return False
        if value >= bounds[1]:
            return False
        if value % EVEN_DIVISOR != 0:
            return False
    return True

if __name__ == '__main__':
    print(is_valid_triplet(10, 20, 30))
    print(is_valid_triplet(0, 20, 30))
    print(is_valid_triplet(10, 20, 100))
    print(is_valid_triplet(10, 21, 30))