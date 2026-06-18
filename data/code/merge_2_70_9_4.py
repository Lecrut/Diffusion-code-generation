from decimal import Decimal, getcontext
getcontext().prec = 50
def compare_distances(distance_a: str, distance_b: str) -> int:
    val_a = Decimal(distance_a)
    val_b = Decimal(distance_b)
    if val_a < val_b:
        return -1
    elif val_a > val_b:
        return 1
    else:
        return 0
if __name__ == '__main__':
    dist_1 = "9876543210987654321"
    dist_2 = "12345678901234567890"
    result = compare_distances(dist_1, dist_2)
    if result == -1:
        print(f"{dist_1} is smaller than {dist_2}")
    elif result == 0:
        print(f"{dist_1} equals {dist_2}")
    else:
        print(f"{dist_1} is larger than {dist_2}")