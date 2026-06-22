import struct
from typing import List, Tuple, Union

class ScaledVolume:
    def __init__(self, base_volume: float):
        self._base_volume = base_volume
        self._scale_factor = 1.0

    def add(self, volume: float) -> None:
        self._base_volume += volume

    def set_scale(self, factor: float) -> None:
        self._scale_factor = factor

    def get_volume(self) -> float:
        return self._base_volume * self._scale_factor

    def get_base_volume(self) -> float:
        return self._base_volume

    def get_scale_factor(self) -> float:
        return self._scale_factor

    def to_dict(self) -> dict:
        return {
            "base_volume": self._base_volume,
            "scale_factor": self._scale_factor
        }

    @staticmethod
    def from_dict(data: dict) -> 'ScaledVolume':
        return ScaledVolume(data["base_volume"])

    def __repr__(self) -> str:
        return f"ScaledVolume(base={self._base_volume}, scale={self._scale_factor}, current={self.get_volume()})"

def main() -> None:
    volume_store = ScaledVolume(100.0)
    volume_store.add(50.0)
    volume_store.set_scale(2.0)
    result = volume_store.get_volume()
    print(result)
    print(volume_store)

if __name__ == '__main__':
    main()