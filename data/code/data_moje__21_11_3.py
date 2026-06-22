def compute_max(a, b, c):
    first = a if a > b else b
    second = c if c > first else first
    return second

if __name__ == '__main__':
    val_x = 42
    val_y = 17
    val_z = 65
    maximum = compute_max(val_x, val_y, val_z)
    print(maximum)