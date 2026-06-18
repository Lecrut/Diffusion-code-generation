import threading
from typing import Dict, Any
class ThreadSafeConfig:
    def __init__(self, config_data: Dict[str, str]):
        self._config = dict(config_data)
        self._lock = threading.Lock()
    @property
    def region_colors(self) -> Dict[str, str]:
        with self._lock:
            return dict(self._config)
def create_config(region_map: Dict[str, Any]) -> ThreadSafeConfig:
    cleaned_data = {k: v if isinstance(v, (str, int)) else "default" for k, v in region_map.items()}
    return ThreadSafeConfig(cleaned_data)
if __name__ == '__main__':
    sample_config = {"us-east": "#FF5733", "eu-west": "#C70039"}
    config_instance = create_config(sample_config)
    print(config_instance.region_colors)