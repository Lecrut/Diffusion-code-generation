def calculate_prism_volume() -> float:
    base_area: float = 10.0
    height: float = 5.0
    return base_area * height

if __name__ == '__main__':
    result: float = calculate_prism_volume()
    print(result)