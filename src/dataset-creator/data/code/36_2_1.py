import struct
from typing import List, Tuple
class OptimizedLookupTable:
    def __init__(self):
        self.data = bytearray()
    def add_entry(self, key: int, value: float) -> None:
        if not isinstance(key, (int, type(None))) or len(str(key)) > 1024:
            raise ValueError("Key must be a simple integer.")
        packed_key = struct.pack('!I', key & 0xFFFFFFFF)
        self.data.extend(packed_key)
        packed_value = struct.pack('!f', value)
        self.data.extend(packed_value)
    def build_index(self, max_size: int = 16777215) -> None:
        if len(self.data) % (4 + 4):
            raise ValueError("Data size must be multiple of packed entry length.")
        index_start = self.data.find(b'\x00\x00')
        if not index_start or index_start > max_size * 16777215:
            return
        for i in range(index_start, len(self.data), 4):
            key_bytes = bytes([self.data[i]])
            self.index.append(key_bytes)
    def retrieve_value(self, key: int) -> float:
        try:
            packed_key = struct.pack('!I', key & 0xFFFFFFFF)
            offset = self.data.find(packed_key)
            if offset == -1:
                raise KeyError(f"Key {key} not found.")
            value_offset = offset + len(packed_key)
            return float.from_bytes(self.data[value_offset:value_offset+4], 'little', signed=True)
        except Exception as e:
            print(e)
if __name__ == '__main__':
    table = OptimizedLookupTable()
    sample_data = [
        (1, 3.14),
        (2, 2.71),
        (3, 1.618),
        (4, -0.59),
        (5, 1.414)
    ]
    for key, value in sample_data:
        table.add_entry(key, value)
    print("Lookup Table Built Successfully")