import math
from typing import List, Optional, Tuple

class CompressedVolumeData:
    def __init__(self, dimensions: List[int], values: List[float], scale_factor: float = 1.0):
        if len(dimensions) != 3:
            raise ValueError("Dimensions must be a list of 3 integers.")
        total_size = 1
        for d in dimensions:
            if d <= 0:
                raise ValueError("Dimensions must be positive integers.")
            total_size *= d
        if len(values) != total_size:
            raise ValueError(f"Values length {len(values)} does not match total dimension size {total_size}.")
        
        self.dimensions = tuple(dimensions)
        self.scale_factor = float(scale_factor)
        self._compressed_data = self._compress(values)

    def _compress(self, values: List[float]) -> List[float]:
        if not values:
            return []
        non_zero_indices = []
        non_zero_values = []
        for i, val in enumerate(values):
            if val != 0.0:
                non_zero_indices.append(i)
                non_zero_values.append(val)
        if len(non_zero_values) == len(values):
            return values
        return {
            "indices": non_zero_indices,
            "values": non_zero_values,
            "dims": self.dimensions,
            "length": len(values)
        }

    def _decompress(self) -> List[float]:
        if isinstance(self._compressed_data, list):
            return self._compressed_data
        data = self._compressed_data
        length = data["length"]
        result = [0.0] * length
        for idx, val in zip(data["indices"], data["values"]):
            result[idx] = val
        return result

    def get_value(self, coords: Tuple[int, int, int]) -> float:
        if len(coords) != 3:
            raise ValueError("Coordinates must be a tuple of 3 integers.")
        x, y, z = coords
        dims = self.dimensions
        if not (0 <= x < dims[0] and 0 <= y < dims[1] and 0 <= z < dims[2]):
            raise ValueError("Coordinates out of bounds.")
        
        values = self._decompress()
        total_cols = dims[1] * dims[2]
        row_size = dims[2]
        
        linear_index = x * total_cols + y * row_size + z
        return values[linear_index]

    def set_value(self, coords: Tuple[int, int, int], value: float) -> None:
        if len(coords) != 3:
            raise ValueError("Coordinates must be a tuple of 3 integers.")
        x, y, z = coords
        dims = self.dimensions
        if not (0 <= x < dims[0] and 0 <= y < dims[1] and 0 <= z < dims[2]):
            raise ValueError("Coordinates out of bounds.")
        
        if isinstance(self._compressed_data, list):
            total_cols = dims[1] * dims[2]
            row_size = dims[2]
            linear_index = x * total_cols + y * row_size + z
            self._compressed_data[linear_index] = value
            if value != 0.0:
                self._compressed_data = list(self._compressed_data)
        else:
            current_non_zero = set(self._compressed_data["indices"])
            total_cols = dims[1] * dims[2]
            row_size = dims[2]
            linear_index = x * total_cols + y * row_size + z
            
            if value != 0.0:
                current_non_zero.add(linear_index)
            else:
                current_non_zero.discard(linear_index)
            
            sorted_indices = sorted(list(current_non_zero))
            new_values = []
            for idx in sorted_indices:
                temp_dims = self._compressed_data["dims"]
                temp_size = 1
                temp_d = 0
                for dim in temp_dims:
                    temp_size *= dim
                
                temp_x = idx // (temp_dims[1] * temp_dims[2])
                temp_remainder = idx % (temp_dims[1] * temp_dims[2])
                temp_y = temp_remainder // temp_dims[2]
                temp_z = temp_remainder % temp_dims[2]
                
                if 0 <= temp_x < temp_dims[0] and 0 <= temp_y < temp_dims[1] and 0 <= temp_z < temp_dims[2]:
                    temp_idx = temp_x * (temp_dims[1] * temp_dims[2]) + temp_y * temp_dims[2] + temp_z
                    if temp_idx == idx:
                        val = self._compressed_data["values"][sorted_indices.index(idx)]
                        new_values.append(val)
            
            self._compressed_data = {
                "indices": sorted_indices,
                "values": new_values,
                "dims": self.dimensions,
                "length": self.dimensions[0] * self.dimensions[1] * self.dimensions[2]
            }

    def scale_by(self, factor: float) -> None:
        self.scale_factor *= factor
        if isinstance(self._compressed_data, list):
            self._compressed_data = [v * factor for v in self._compressed_data]
        else:
            self._compressed_data["values"] = [v * factor for v in self._compressed_data["values"]]

    def get_scaled_value(self, coords: Tuple[int, int, int]) -> float:
        val = self.get_value(coords)
        return val * self.scale_factor

    def get_sum(self) -> float:
        values = self._decompress()
        return sum(values)

def main():
    dims = [2, 3, 4]
    vals = [1.0, 0.0, 0.0, 2.0, 3.0, 0.0, 0.0, 4.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 6.0, 7.0, 0.0, 0.0, 0.0, 0.0, 8.0, 0.0, 0.0, 0.0]
    volume = CompressedVolumeData(dims, vals, 2.0)
    
    val_x0y0z0 = volume.get_scaled_value((0, 0, 0))
    val_x1y2z3 = volume.get_scaled_value((1, 2, 3))
    total_sum = volume.get_sum()
    
    print(val_x0y0z0)
    print(val_x1y2z3)
    print(total_sum)
    
    volume.set_value((0, 0, 0), 10.0)
    val_x0y0z0_after_set = volume.get_scaled_value((0, 0, 0))
    print(val_x0y0z0_after_set)
    
    volume.scale_by(0.5)
    val_x0y0z0_after_scale = volume.get_scaled_value((0, 0, 0))
    print(val_x0y0z0_after_scale)

if __name__ == '__main__':
    main()