HALF = 0.5

triangle_area = lambda base, height: HALF * base * height

if __name__ == '__main__':
    sample_values = [14, 7]
    print(triangle_area(*sample_values))