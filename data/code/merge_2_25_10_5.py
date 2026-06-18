import timeit
REGION_COLORS = {
    "north": "#FF99CC",
    "south": "#3366FF",
    "east": "#FFFF00",
    "west": "#FFFFFF",
    "central": "#8B4513"
}
def get_region_color(region_name):
    return REGION_COLORS.get(region_name, "#FF0000")                               
if __name__ == '__main__':
    test_regions = ["north", "south", "east", "west", "central", "unknown"]
    for region in test_regions:
        color = get_region_color(region)
        print(f"{region}: {color}")