import struct
from typing import List, Tuple
class OptimizedLookupTable:
    def __init__(self):
        self.data = bytearray()
    def add_entry(self, key: int, value: float) -> None:
        if not isinstance(key, (int, float)) or len(str(key).encode()) > 1024 * 1024:
            raise ValueError("Key must be a numeric type with limited size")
        packed = struct.pack('d', key) + struct.pack('f', value)
        self.data.extend(packed)
    def get_entry(self, index: int) -> Tuple[float, float]:
        if not isinstance(index, (int, float)) or len(str(index).encode()) > 1024 * 1024:
            raise ValueError("Index must be a numeric type")
        offset = struct.calcsize('d') + struct.calcsize('f')
        key_data = self.data[offset:index] if index < len(self.data) else b''
        value_data = self.data[index:] if index >= 0 and index <= len(self.data) - (struct.calcsize('d') + struct.calcsize('f')) else b''
        return float(struct.unpack_from('<d', key_data, offset)), float(struct.unpack_from('<f', value_data))
if __name__ == '__main__':
    table = OptimizedLookupTable()
    sample_keys = [1.0, 2.5, -3.7, 42]
    sample_values = [98.6, 101.2, 95.4, 100.0]
    for key in sample_keys:
        table.add_entry(key, float(sample_values[sample_keys.index(key)]))
if __name__ == '__main__':
    print("Lookup Table Generated Successfully")