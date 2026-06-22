def calculate_cone_volume(radius, height):
    return (1/3) * 3.141592653589793 * radius**2 * height

if __name__ == '__main__':
    result = calculate_cone_volume(5, 10)
    print(result)