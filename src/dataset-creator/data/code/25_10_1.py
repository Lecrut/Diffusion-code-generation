import json
REGION_COLOR_MAP = {
    "north": "#FF99CC",
    "south": "#00FFFF",
    "east": "#FFFF00",
    "west": "#CC00FF",
    "central": "#FFFFFF"
}
def get_region_color(region_name: str) -> str | None:
    return REGION_COLOR_MAP.get(region_name.lower())
if __name__ == '__main__':
    test_regions = ["north", "south", "east", "west", "unknown"]
    for region in test_regions:
        color_code = get_region_color(region)
        print(f"Region '{region}': {color_code}")