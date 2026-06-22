def compare_values(a, b):
    return a if a > b else b

def find_maximum(x, y, z):
    lookup_map = {
        'first': x,
        'second': y,
        'third': z
    }
    values = [lookup_map[k] for k in lookup_map]
    current_max = values[0]
    for val in values[1:]:
        current_max = compare_values(current_max, val)
    return current_max

if __name__ == '__main__':
    val_a = 42
    val_b = 17
    val_c = 99
    result = find_maximum(val_a, val_b, val_c)
    print(result)