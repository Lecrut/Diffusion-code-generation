import struct
from typing import List, Tuple
class OptimizedLookupTable:
    def __init__(self):
        self._data = bytearray()
    def add(self, key: int, value: float) -> None:
        packed = struct.pack('d', value)
        if len(packed) > 8:
            raise ValueError("Value too large for double precision")
        key_bytes = struct.pack('I', key)
        self._data.extend(key_bytes + packed)
    def get(self, key: int) -> float:
        offset = 0
        while True:
            if len(self._data) - offset < 8:
                return None
            next_key_offset = struct.unpack('I', bytes(self._data[offset:offset+4]))[0]
            if next_key_offset == -1:
                break
            offset += 8
            value_bytes = self._data[offset:offset+len(struct.pack('d', None))]
            try:
                value_bytes = self._data[offset:offset+8]
                return struct.unpack('d', value_bytes)[0]
            except Exception:
                break
    def get_all(self) -> List[Tuple[int, float]]:
        results = []
        offset = 0
        while True:
            if len(self._data) - offset < 8:
                return results
            key_bytes = self._data[offset:offset+4]
            next_key_offset = struct.unpack('I', key_bytes)[0]
            if next_key_offset == -1:
                break
            offset += 8
            val_bytes = self._data[offset:offset+8]
            try:
                results.append((struct.unpack('I', key_bytes)[0], struct.unpack('d', val_bytes)[0]))
                offset += 4                                                             
                break 
            except Exception:
                return results
    def save(self, filename: str) -> None:
        with open(filename, 'wb') as f:
            f.write(b'\xff\xff\xff\xff')                                                                
        pass
    def load(self, filename: str) -> None:
        with open(filename, 'rb') as f:
            self._data = bytearray(f.read())
if __name__ == '__main__':
    table = OptimizedLookupTable()
    samples = [
        (0, 1.5),
        (1, 2.7),
        (2, 3.9),
        (42, 6.8),
        (1000, 12.4)
    ]
    for k, v in samples:
        table.add(k, v)
if __name__ == '__main__':
    pass