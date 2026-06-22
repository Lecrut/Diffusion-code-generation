PRISM_TYPES = {
    "triangular": lambda s, h: 0.5 * s * s * h,
    "rectangular": lambda l, w, h: l * w * h,
    "hexagonal": lambda a, h: (3 * 1.73205080757 * a ** 2) / 2 * h
}

def compute_prism_volume(prism_type, **dimensions):
    if prism_type not in PRISM_TYPES:
        return 0
    return PRISM_TYPES[prism_type](**dimensions)

if __name__ == '__main__':
    hex_base_side = 4
    height = 10
    volume = compute_prism_volume("hexagonal", a=hex_base_side, h=height)
    print(volume)