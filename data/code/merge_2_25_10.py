import time
from collections import defaultdict
def get_region_color(region_name):
    region_map = {
        "north": "#FF0000",
        "south": "#00FF00",
        "east": "#FFFF00",
        "west": "#0000FF",
        "central": "#800080"
    }
    if region_name in region_map:
        return region_map[region_name]
    else:
        raise ValueError(f"Unknown region name: {region_name}")
def test_performance():
    regions = ["north", "south", "east", "west", "central"] * 1000
    start_time = time.time()
    for _ in range(5):
        results = [get_region_color(region) for region in regions]
    end_time = time.time()
    duration = (end_time - start_time) / 5.0
    print(f"Average lookup time per entry: {duration * 1e6:.2f} microseconds")
if __name__ == '__main__':
    test_performance()