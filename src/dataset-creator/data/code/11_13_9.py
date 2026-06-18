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
    sample_list = [1, 5, 2, 8, 3]
    total, prod, min_val, max_val = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    empty_list = []
    total_e, prod_e, min_e, max_e = analyze_list(empty_list)
    print(f"\nList: {empty_list}")
    print(f"Sum: {total_e}")
    print(f"Product: {prod_e}")
    print(f"Minimum: {min_e}")
    print(f"Maximum: {max_e}")