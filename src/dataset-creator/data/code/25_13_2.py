import threading
from typing import Dict, Any
class RegionColorConfig:
    def __init__(self, config: Dict[str, str]):
        self._lock = threading.Lock()
        with self._lock:
            self._data = dict(config)
    @property
    def data(self) -> Dict[str, str]:
        return dict(self._data)
def create_config_instance(config_dict: Dict[str, Any]) -> RegionColorConfig:
    with threading.Lock():
        config = {k: v for k, v in config_dict.items() if isinstance(v, str)}
    return RegionColorConfig(config)
if __name__ == '__main__':
    sample_config = {'us-east-1': '#3b82f6', 'eu-west-1': '#ef4444'}
    instance = create_config_instance(sample_config)