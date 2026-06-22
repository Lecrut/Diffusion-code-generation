def compute_prism_volume(base_area: float, height: float) -> float:
    return base_area * height

if __name__ == '__main__':
    result = compute_prism_volume(10.0, 5.0)
    print(result)