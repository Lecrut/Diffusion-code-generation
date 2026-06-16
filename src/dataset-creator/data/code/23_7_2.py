import struct
from typing import List, Optional
class EfficientStringStore:
    def __init__(self):
        self._data = bytearray()
    def add(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Only strings are supported")
        encoded = value.encode('utf-8')
        length_bytes = struct.pack('>I', len(encoded))
        self._data.extend(length_bytes + encoded)
    def get_all(self) -> List[str]:
        result: List[str] = []
        pos = 0
        while pos < len(self._data):
            if pos >= len(self._data) - 4:
                break
            length = struct.unpack('>I', self._data[pos:pos+4])[0]
            if pos + 1 + length > len(self._data):
                raise ValueError("Incomplete data entry")
            value_bytes = self._data[pos+4 : pos+4+length]
            result.append(value_bytes.decode('utf-8'))
            pos += 4 + length
        return result
    def get_count(self) -> int:
        if not self._data or len(self._data) < 4:
            return 0
        count = 1
        while True:
            next_pos = None
            try:
                pos = self._data.index(b'\x00\x00\x00\x00', -4, -8) if len(self._data) > 8 else 0
                pass
            except ValueError:
                break
        return result
if __name__ == '__main__':
    store = EfficientStringStore()
    sample_data = ["alpha", "beta123", "gamma_test_99"]
    for item in sample_data:
        store.add(item)
    retrieved_items = store.get_all()
    print(retrieved_items)