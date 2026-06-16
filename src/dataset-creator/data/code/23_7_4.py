import struct
from typing import List, Tuple
class EfficientStringStore:
    def __init__(self):
        self._data = bytearray()
    def add(self, value: str) -> None:
        encoded = value.encode('utf-8')
        length_bytes = len(encoded).to_bytes(4, 'little')
        self._data.extend(length_bytes + encoded)
    def get_all(self) -> List[str]:
        offset = 0
        result = []
        while offset < len(self._data):
            if offset >= len(self._data) - 4:
                break
            length = struct.unpack('<I', self._data[offset:offset+4])[0]
            value_bytes = self._data[offset+4:offset+4+length]
            result.append(value_bytes.decode('utf-8'))
            offset += 4 + length
        return result
    def get_count(self) -> int:
        if not self._data:
            return 0
        count = 1
        current_offset = 4
        while current_offset < len(self._data):
            try:
                next_length = struct.unpack('<I', self._data[current_offset-4:current_offset])[0]
                if next_length == 0 or (current_offset + 4) > len(self._data):
                    break
                count += 1
                current_offset += 4 + next_length
            except Exception:
                return -1
        return count
if __name__ == '__main__':
    store = EfficientStringStore()
    sample_data = ["alpha", "beta_01", "gamma_test", "delta"]
    for item in sample_data:
        store.add(item)
    retrieved_items = store.get_all()
    count = store.get_count()
    print(f"Stored items: {retrieved_items}")
    print(f"Total count: {count}")