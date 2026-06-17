def compare_distances(distance_a: int | float, distance_b: int | float) -> str:
    val_a = int(distance_a) if isinstance(distance_a, float) and distance_a.is_integer() else distance_a
    val_b = int(distance_b) if isinstance(distance_b, float) and distance_b.is_integer() else distance_b
    if val_a < val_b:
        return "distance_a is smaller"
    elif val_b < val_a:
        return "distance_b is smaller"
    else:
        return "distances are equal"
if __name__ == '__main__':
    dist_1 = 50000000000000000000000000000000