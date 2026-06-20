def scale_volumes(volumes: list[float], factor: float) -> list[float]:
    return [v * factor for v in volumes]

if __name__ == '__main__':
    volumes = [10.0, 20.0, 30.0]
    factor = 1.5
    result = scale_volumes(volumes, factor)
    print(result)