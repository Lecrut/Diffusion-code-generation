def analyze_list(data):
    if not data:
        return None, None, None, None
    total_sum = sum(data)
    product = 1
    for x in data:
        product *= x
    minimum = min(data)
    maximum = max(data)
    return total_sum, product, minimum, maximum
if __name__ == '__main__':
    sample_list = [10, 5, 2, 8, 1]
    total, prod, min_val, max_val = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    sample_list_2 = [-5, 100, 0, -20]
    total_2, prod_2, min_val_2, max_val_2 = analyze_list(sample_list_2)
    print(f"\nList: {sample_list_2}")
    print(f"Sum: {total_2}")
    print(f"Product: {prod_2}")
    print(f"Minimum: {min_val_2}")
    print(f"Maximum: {max_val_2}")