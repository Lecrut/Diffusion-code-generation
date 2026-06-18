import threading
class RegionColorMap:
    def __init__(self):
        self._lock = threading.Lock()
        self._data = {}
    def set_region_color(self, region_name, color):
        with self._lock:
            self._data[region_name] = color
    def get_region_colors(self) -> dict:
        with self._lock:
            return dict(self._data)
if __name__ == '__main__':
    config_map = RegionColorMap()
    configs = [
        {"regions": ["us-east", "eu-west"], "colors": ["#FF5733", "#3498DB"]},
        {"regions": ["ap-south", "sa-east"], "colors": ["#F1C40F", "#2ECC71"]}
    ]
    for cfg in configs:
        region_names = list(cfg["regions"])
        colors = dict(zip(region_names, cfg["colors"]))
        config_map.set_region_color(*region_names)                                                                                                                                        
    final_colors = config_map.get_region_colors()
    print(final_colors)