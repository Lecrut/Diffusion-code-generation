import struct
from typing import Dict, Tuple
class OptimizedLookupTable:
    def __init__(self):
        self._data = {}
    def add_entry(self, key: int, value: float) -> None:
        if not isinstance(key, (int, str)) or not isinstance(value, (float, int)):
            raise TypeError("Key must be hashable and value must be numeric")
        self._data[key] = struct.pack('d', float(value))
    def get_entry(self, key: any) -> Tuple[bool, bytes]:
        if key in self._data:
            return True, self._data[key]
        return False, b''
def generate_table() -> OptimizedLookupTable:
    table = OptimizedLookupTable()
    base_values = [1.0, 2.5, -3.7, 4.89e-6]
    for i in range(1_000_000):
        key_val = f"{i:08d}"
        value_idx = (hash(key_val) % len(base_values))
        table.add_entry(int(i), base_values[value_idx])
if __name__ == '__main__':
    lt = generate_table()