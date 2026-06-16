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
            return self._config.get(region_name)
    def update_region_color(self, region_name: str, color: str):
        with self._lock:
            if region_name in self._config:
                self._config[region_name] = color
if __name__ == '__main__':
    initial_config = {
        "us-east": "#FF5733",
        "eu-west": "#3498DB",
        "ap-south": "#2ECC71"
    }
    config_instance = RegionColorConfig.from_dict(initial_config)
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda: None, args=(config_instance.get("us-east"),))
        threads.append(t)
    for t in threads:
        t.start()
    config_instance.update_region_color("eu-west", "#E74C3C")