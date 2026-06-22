def get_first_item(items):
    if not items:
        raise IndexError("List is empty, cannot retrieve first item")
    return items[0]

def run_demo():
    config_map = {
        "numbers": [100, 200, 300],
        "letters": ["a", "b", "c"],
        "mixed": [1, "x", 3.14]
    }
    results = []
    for key in config_map:
        val = get_first_item(config_map[key])
        results.append((key, val))
    for k, v in results:
        print(f"{k}: {v}")

if __name__ == '__main__':
    run_demo()