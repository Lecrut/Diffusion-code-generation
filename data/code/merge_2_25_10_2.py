import timeit
def get_region_color(region_name):
    region_colors = {
        "north": "#FF7F50",
        "south": "#2E8B57",
        "east": "#4169E1",
        "west": "#DC143C",
        "central": "#FFFF00"
    }
    return region_colors.get(region_name, "#FFFFFF")
if __name__ == '__main__':
    test_regions = ["north", "south", "east", "unknown"]
    for region in test_regions:
        color_code = get_region_color(region)
        print(f"{region}: {color_code}")
    time_taken = timeit.timeit(stmt=get_region_color("north"), number=10000)
    print(f"Time taken for 10,000 lookups: {time_taken:.4f} seconds")