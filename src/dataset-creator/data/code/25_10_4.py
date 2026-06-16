import timeit
REGION_COLORS = {
    "north": "#FF0000",
    "south": "#00FF00",
    "east": "#FFFF00",
    "west": "#0000FF",
    "central": "#808080"
}
def get_region_color(region_name):
    return REGION_COLORS.get(region_name, "#FFFFFF")
if __name__ == '__main__':
    samples = ["north", "south", "east", "west", "central", "unknown"]
    for region in samples:
        color = get_region_color(region)
        print(f"{region}: {color}")
    iterations = 1000000
    start_time = timeit.default_timer()
    for _ in range(iterations):
        result = REGION_COLORS.get("north", "#FFFFFF")
    end_time = timeit.default_timer()
    elapsed_seconds = end_time - start_time
    print(f"Average lookup time per region: {elapsed_seconds / iterations * 1000:.6f} ms")