def compute_area(side_length):
    if side_length < 0:
        return 0
    return side_length ** 2

if __name__ == '__main__':
    side = 7
    result = compute_area(side)
    print(result)