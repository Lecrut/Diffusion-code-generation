SIDE_LENGTH_DEFAULT = 7

def get_area(side):
    return side * side

def main():
    side = SIDE_LENGTH_DEFAULT
    area = get_area(side)
    print(area)

if __name__ == '__main__':
    main()