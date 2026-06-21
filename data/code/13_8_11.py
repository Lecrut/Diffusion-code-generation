from collections import defaultdict

def get_with_composite_key(data, key1, key2, factory):
    return data[key1][key2] if key1 in data and key2 in data[key1] else data[key1].setdefault(key2, factory())

def run_demo():
    dd = defaultdict(lambda: defaultdict(lambda: 0))
    result1 = get_with_composite_key(dd, "groupA", "itemX", lambda: 100)
    result2 = get_with_composite_key(dd, "groupA", "itemY", lambda: 200)
    result3 = get_with_composite_key(dd, "groupA", "itemX", lambda: 999)
    dd["groupB"]["itemZ"] = 50
    result4 = get_with_composite_key(dd, "groupB", "itemZ", lambda: 999)
    print(result1)
    print(result2)
    print(result3)
    print(result4)

if __name__ == '__main__':
    run_demo()