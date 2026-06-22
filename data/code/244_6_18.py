def calculate_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

if __name__ == '__main__':
    diagonals1 = [6, 8]
    diagonals2 = [10, 12]
    
    area1 = calculate_area(*diagonals1)
    area2 = calculate_area(*diagonals2)
    
    print(area1 + area2)