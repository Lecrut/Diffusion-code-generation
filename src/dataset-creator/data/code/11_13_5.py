def analyze_list(data):
    if not data:
        return None, None, None, None
    total_sum = sum(data)
    total_product = 1
    for x in data:
        total_product *= x
    minimum = min(data)
    maximum = max(data)
    return total_sum, total_product, minimum, maximum
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    total, product, minimum, maximum = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Product: {product}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")