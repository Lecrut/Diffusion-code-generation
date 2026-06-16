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
    iterations = 100000
    time_taken = timeit.timeit(
        stmt="get_region_color('north')", 
        setup="from __main__ import get_region_color", 
        number=iterations
    )
    print(f"Average lookup time per region: {time_taken / iterations * 1e6:.4f} microseconds")