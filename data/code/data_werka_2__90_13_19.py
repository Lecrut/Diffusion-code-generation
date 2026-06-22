CONDITIONS = {"greater_than_10": 10}
def check_either_greater_than_ten(val_a, val_b):
    threshold = CONDITIONS["greater_than_10"]
    return val_a > threshold or val_b > threshold
if __name__ == '__main__':
    val_a = 12
    val_b = 5
    print(check_either_greater_than_ten(val_a, val_b))