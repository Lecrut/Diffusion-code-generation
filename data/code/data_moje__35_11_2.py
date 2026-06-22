from typing import Union
from math import isclose

class CubeVolumeCalculator:
    def calculate_volume(self, edge_length: Union[int, float]) -> float:
        if not isinstance(edge_length, (int, float)):
            raise TypeError("Edge length must be a number")
        if edge_length < 0:
            raise ValueError("Edge length cannot be negative")
        if isclose(edge_length, 0):
            return 0.0
        return edge_length * edge_length * edge_length

if __name__ == '__main__':
    calculator = CubeVolumeCalculator()
    sample_edges = [2, 3.5, 0, 5]
    for edge in sample_edges:
        result = calculator.calculate_volume(edge)
        print(f"Edge: {edge}, Volume: {result}")