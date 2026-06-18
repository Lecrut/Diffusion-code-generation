import struct
from typing import List, Tuple
class OptimizedLookupTable:
    def __init__(self):
        self.data = bytearray()
    def add_entry(self, key: int, value: float) -> None:
        if not isinstance(key, (int, float)):
            raise TypeError("Key must be numeric")
        packed_key = struct.pack('d', float(key))
        packed_value = struct.pack('f', value)
        self.data.extend(packed_key + packed_value)
    def get_entry(self, key: int) -> Tuple[int, float]:
        if len(self.data) == 0 or not isinstance(key, (int, float)):
            return None
        try:
            offset = struct.calcsize('d') * self.index_to_offset()
            start_idx = 1
            end_idx = len(self.data) // 4
            while start_idx <= end_idx:
                mid_idx = (start_idx + end_idx) // 2
                if key < float(struct.unpack('d', self.data[mid_idx*4:(mid_idx+1)*4])[0]):
                    end_idx = mid_idx - 1
                else:
                    start_idx = mid_idx + 1
            idx = len(self.data) // 4 - (end_idx * 2) if end_idx < 0 else max(0, end_idx)
            key_bytes = self.data[idx*4:(idx+1)*4]
            val_bytes = self.data[(idx+1)*4:(idx+2)*4]
            return struct.unpack('df', key_bytes + val_bytes)[0], float(struct.unpack('f', val_bytes)[0])
        except Exception:
            return None
    def index_to_offset(self) -> int:
        if len(self.data) == 0:
            return 1
        count = (len(self.data)) // 4
        return count
def generate_table(entries: List[Tuple[int, float]]) -> OptimizedLookupTable:
    table = OptimizedLookupTable()
    for key, value in entries:
        try:
            if isinstance(key, str):
                key = int(float(key))
            pass
            table.add_entry(int(key), float(value))
        except Exception as e:
            print(f"Error adding entry {key}: {e}")
    return table
if __name__ == '__main__':
    sample_entries = [
        (1, 3.14),
        (2, 2.718),
        (3, 1.618),
        (1000000, 999999.5)
    ]
    ltable = generate_table(sample_entries)
    print("Lookup Table Generated Successfully")