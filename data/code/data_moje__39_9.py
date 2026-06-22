def calculate_prism_volume() -> float:
    base_area: float = 10.0
    height: float = 5.0
    volume: float = base_area * height
    return volume

if __name__ == '__main__':
    result = calculate_prism_volume()
    print(result)