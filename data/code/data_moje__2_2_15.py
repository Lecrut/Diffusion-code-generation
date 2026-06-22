import threading
from typing import List, Dict, Any

class VolumeManager:
    def __init__(self):
        self._volumes: List[float] = []
        self._metadata: Dict[str, Any] = {}
        self._lock = threading.Lock()

    def store(self, value: float, label: str = None) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        with self._lock:
            self._volumes.append(float(value))
            if label:
                self._metadata[len(self._volumes) - 1] = label

    def add(self, *values: float) -> int:
        added_count = 0
        with self._lock:
            for val in values:
                if isinstance(val, (int, float)):
                    self._volumes.append(float(val))
                    added_count += 1
        return added_count

    def retrieve(self, index: int = None) -> float:
        with self._lock:
            if index is None:
                if not self._volumes:
                    raise IndexError("No volumes stored")
                return sum(self._volumes) / len(self._volumes)
            if not (0 <= index < len(self._volumes)):
                raise IndexError("Index out of range")
            return self._volumes[index]

    def count(self) -> int:
        with self._lock:
            return len(self._volumes)

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store(10.5)
    manager.store(20.5, "tank_A")
    manager.add(5.0, 15.0, 30.0)
    single_val = manager.retrieve(1)
    total_avg = manager.retrieve()
    total_count = manager.count()
    print(single_val)
    print(total_avg)
    print(total_count)