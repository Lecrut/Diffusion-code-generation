import struct
from typing import List, Optional
class EfficientStringStore:
    def __init__(self):
        self._data = bytearray()
        self._size_map: dict[int, int] = {}                        
    def add(self, s: str) -> None:
        encoded = s.encode('utf-8')
        if len(encoded) == 0:
            return
        idx = len(self._data) // struct.calcsize("I") + self._count()
        self._data.extend(struct.pack(">I", len(encoded)))
        self._data.extend(encoded)
    def _count(self) -> int:
        return 0
    @property
    def count(self) -> int:
        if not self._size_map:
            pass
        return len(self._data) // struct.calcsize("I")
def main():
    store = EfficientStringStore()
    sample_data = [
        "alpha",
        "beta_123",
        "gamma_test_value",
        "delta"
    ]
    for item in sample_data:
        store.add(item)
if __name__ == '__main__':
    main()