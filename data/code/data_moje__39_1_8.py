def compute_prism_volume(base_area: float, height: float) -> float:
    if base_area <= 0 or height <= 0:
        raise ValueError("Base area and height must be positive")
    return base_area * height

if __name__ == '__main__':
    base_area: float = 10.0
    height: float = 5.0
    volume: float = compute_prism_volume(base_area, height)
    print(volume)