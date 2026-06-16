import timeit
def get_region_color(region_name):
    region_colors = {
        "north": "#FF7F50",
        "south": "#2E8B57",
        "east": "#4169E1",
        "west": "#DC143C",
        "central": "#DAA520"
    }
    if region_name in region_colors:
        return region_colors[region_name]
    else:
        raise ValueError(f"No color found for region '{region_name}'")
if __name__ == '__main__':
    test_regions = ["north", "south", "east", "west"]
    iterations = 10000
    print("Testing Region Color Mapping...")
    for region in test_regions:
        color = get_region_color(region)
        time_taken = timeit.timeit(f"get_region_color('{region}')", globals=globals(), number=iterations) / iterations * 1e6
        print(f"{region}: {color} (Avg lookup time: {time_taken:.4f} microseconds)")
    try:
        get_region_color("unknown")
    except ValueError as e:
        print(f"Error caught for unknown region: {e}")