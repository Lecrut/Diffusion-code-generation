from itertools import product

def get_xor_outputs():
    outputs = list(product((0, 1), repeat=2))
    rows = []
    for a, b in outputs:
        val = 0 if a == b else 1
        rows.append((a, b, val))
    return rows

if __name__ == '__main__':
    data = get_xor_outputs()
    for item in data:
        print(item)