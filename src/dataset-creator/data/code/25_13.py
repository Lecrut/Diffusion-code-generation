import threading
from typing import Dict, Any
class RegionColorConfig:
    def __init__(self, config_dict: Dict[str, str]):
        self._config = dict(config_dict)
        self._lock = threading.Lock()
    @classmethod
    def from_config(cls, raw_config: Dict[str, str]) -> 'RegionColorConfig':
        instance = cls(raw_config.copy())
        return instance
    def get_color(self, region_name: str) -> Any:
        with self._lock:
            if region_name in self._config:
                return self._config[region_name]
            raise KeyError(f"Region '{region_name}' not found")
    def update_region(self, region_name: str, color: str):
        with self._lock:
            self._config[region_name] = color
if __name__ == '__main__':
    sample_config = {
        "us-east": "#FF5733",
        "eu-west": "#3498DB",
        "ap-south": "#2ECC71"
    }
    config_instance = RegionColorConfig.from_config(sample_config)
    print(config_instance.get_color("us-east"))                   
    threads = []
    for i in range(5):
        t = threading.Thread(target=lambda c=config_instance, r=f"region-{i}": c.update_region(r, f"#COLOR{i}"))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(config_instance.get_color("region-0"))