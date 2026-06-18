def analyze_list(data):
    if not data:
        return None, None, None, None
    total_sum = 0
    product = 1
    minimum = data[0]
    maximum = data[0]
    for x in data:
        total_sum += x
        product *= x
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
    return total_sum, product, minimum, maximum
if __name__ == '__main__':
    sample_list = [10, 20, 5, 30, 15]
    total, prod, min_val, max_val = analyze_list(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")