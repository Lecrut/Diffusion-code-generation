import math
from collections import defaultdict

class VolumeManager:
    def __init__(self):
        self._measurements = defaultdict(float)
        self._history = []

    def store(self, identifier: str, value: float) -> None:
        self._measurements[identifier] = value
        self._history.append((identifier, value))

    def add(self, identifier: str, increment: float) -> float:
        current = self._measurements.get(identifier, 0.0)
        new_value = current + increment
        self._measurements[identifier] = new_value
        self._history.append((identifier, new_value))
        return new_value

    def get(self, identifier: str) -> float:
        return self._measurements.get(identifier, 0.0)

    def get_all(self) -> dict:
        return dict(self._measurements)

    def get_history(self) -> list:
        return list(self._history)

    def remove(self, identifier: str) -> bool:
        if identifier in self._measurements:
            del self._measurements[identifier]
            return True
        return False

if __name__ == '__main__':
    manager = VolumeManager()
    manager.store("box_a", 10.5)
    manager.store("box_b", 20.0)
    new_val = manager.add("box_a", 5.5)
    print(new_val)
    current = manager.get("box_b")
    print(current)
    all_vals = manager.get_all()
    print(all_vals)
    removed = manager.remove("box_a")
    print(removed)
    final_vals = manager.get_all()
    print(final_vals)