area_rhombus = lambda d1, d2: (_ for _ in ()).throw(ValueError("Invalid diagonals")) if d1 <= 0 or d2 <= 0 else d1 * d2 * 0.5
if __name__ == '__main__':
    print(area_rhombus(6.0, 8.0))