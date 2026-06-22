def compute_area(side):
    if side <= 0:
        return 0
    return side ** 2

def main():
    side_length = 10
    area = compute_area(side_length)
    print(area)

if __name__ == '__main__':
    main()