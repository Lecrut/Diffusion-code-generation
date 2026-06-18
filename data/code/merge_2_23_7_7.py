import struct
from typing import List, Tuple
class EfficientStringStore:
    def __init__(self):
        self._data = bytearray()
    def add(self, value: str) -> None:
        encoded = value.encode('utf-8')
        length_bytes = len(encoded).to_bytes(4, byteorder='little')
        self._data.extend(length_bytes)
        self._data.extend(encoded)
    def get_all(self) -> List[str]:
        result = []
        pos = 0
        while pos < len(self._data):
            length_data = self._data[pos:pos+4]
            try:
                string_length = struct.unpack('<I', length_data)[0]
            except Exception as e:
                break
            if pos + 1 + string_length > len(self._data):
                break
            end_pos = pos + 1 + string_length
            value_bytes = self._data[pos+1:end_pos]
            try:
                result.append(value_bytes.decode('utf-8'))
            except UnicodeDecodeError:
                pass
            pos = end_pos
        return result
    def get_count(self) -> int:
        if not self._data:
            return 0
        count = 1
        current_len_data_start = 4
        while current_len_data_start < len(self._data):
            length_bytes = self._data[current_len_data_start-4 : current_len_data_start]
            try:
                string_length = struct.unpack('<I', length_bytes)[0]
                if string_length == 0 or (current_len_data_start + 1 + string_length > len(self._data)):
                    break
                count += 1
                current_len_data_start += 4 + string_length
            except Exception:
                return count
        return max(0, count)
if __name__ == '__main__':
    store = EfficientStringStore()
    sample_values = [
        "alpha",
        "beta_123",
        "gamma_test",
        "delta_final"
    ]
    for val in sample_values:
        store.add(val)
    retrieved_data = store.get_all()
    count = store.get_count()
    print(f"Stored {count} items.")
    for item in retrieved_data:
        print(item)