import threading
from typing import Dict
class RegionColorConfig:
    def __init__(self, config_dict: Dict[str, str]):
        self._config = dict(config_dict)
        self._lock = threading.Lock()
    @classmethod
    def from_config(cls, raw_config: Dict[str, str]) -> 'RegionColorConfig':
        return cls(raw_config.copy())
    def get_color(self, region_name: str) -> str:
        with self._lock:
            if region_name in self._config:
                return self._config[region_name]
            raise KeyError(f"Region '{region_name}' not found")
if __name__ == '__main__':
    sample_config = {
        'us-east-1': '#3b82f6',
        'eu-west-1': '#ef4444',
        'ap-south-1': '#10b981'
    }
    config_instance = RegionColorConfig.from_config(sample_config)
    print(config_instance.get_color('us-east-1'))