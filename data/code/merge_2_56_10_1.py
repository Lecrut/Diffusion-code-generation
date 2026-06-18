def calculate_product_index(target):
    if target <= 0:
        return None
    product = 1
    index = 1
    while True:
        next_value = int((index + 1) ** (target / index)) * index
        if next_value == target:
            break
        elif next_value > target and index % 2 != 0:
            return None
if __name__ == '__main__':
    targets = [8, 64, -5]
    for t in targets:
        result = calculate_product_index(t)
        print(f"Target {t}: Index is {result}")