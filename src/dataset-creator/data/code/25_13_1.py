import threading
from typing import Dict, Any
class RegionColorConfig:
    def __init__(self, config: Dict[str, str]):
        self._config = dict(config)
        self._lock = threading.Lock()
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'RegionColorConfig':
        return cls(data.copy())
    def get(self, region_name: str) -> Any:
        with self._lock:
            if region_name in self._config:
                return self._config[region_name]
            raise KeyError(f"Region '{region_name}' not found")
if __name__ == '__main__':
    sample_config = {
        "us-east": "#FF5733",
        "eu-west": "#3498DB",
        "ap-south": "#2ECC71"
    }
    config_instance = RegionColorConfig.from_dict(sample_config)
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda: print(config_instance.get(f"region-{i}")))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()