DIAGONAL1 = 6
DIAGONAL2 = 8
DIAGONAL3 = 10
DIAGONAL4 = 12

def calculate_area(diagonal1, diagonal2):
    return (diagonal1 * diagonal2) / 2

def calculate_total_area():
    area1 = calculate_area(DIAGONAL1, DIAGONAL2)
    area2 = calculate_area(DIAGONAL3, DIAGONAL4)
    return area1 + area2

if __name__ == '__main__':
    total_area = calculate_total_area()
    print(total_area)