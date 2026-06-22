from collections import defaultdict

def get_or_init(composite_key, factory):
    storage = defaultdict(factory)
    return storage[composite_key]

if __name__ == '__main__':
    key = ("user1", "score")
    result = get_or_init(key, list)
    print(result)