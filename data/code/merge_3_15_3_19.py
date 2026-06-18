def check_equal(x: any = None, y: any = None) -> bool:
    """Returns True if x equals y."""
    return x == y

if __name__ == '__main__':
    sample_x = 10
    sample_y = "Ten"
    print(f"x={sample_x}, y={sample_y} are equal? {check_equal(sample_x, sample_y)}")