from typing import Union

class CubeVolumeCalculator:
    def calculate_volume(self, edge_length: Union[int, float]) -> float:
        if edge_length < 0:
            raise ValueError("Edge length cannot be negative")
        return edge_length ** 3

if __name__ == '__main__':
    calculator = CubeVolumeCalculator()
    edge = 5
    result = calculator.calculate_volume(edge)
    print(result)