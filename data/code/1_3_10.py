import typing

def find_outliers(weights: typing.List[float], min_val: float=50.0, max_val: float=200.0) -> typing.List[float]:
    return [w for w in weights if w < min_val or w > max_val]
if __name__ == '__main__':
    sample_data = [45.0, 50.0, 100.0, 150.0, 200.0, 205.0, 300.0, 0.0]
    result = find_outliers(sample_data)
    print(result)