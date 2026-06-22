def prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    base = 10.0
    height = 5.0
    result = prism_volume(base, height)
    print(result)