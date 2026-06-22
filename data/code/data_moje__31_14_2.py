SIDE_LENGTH = 50

def compute_area(length):
    squared_value = length * length
    return squared_value

if __name__ == '__main__':
    side = SIDE_LENGTH
    area = compute_area(side)
    print(area)