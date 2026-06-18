def calculate_stats(data):
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
    total, prod, minimum, maximum = calculate_stats(sample_list)
    print(f"List: {sample_list}")
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    sample_list_empty = []
    total, prod, minimum, maximum = calculate_stats(sample_list_empty)
    print(f"\nList: {sample_list_empty}")
    print(f"Sum: {total}")
    print(f"Product: {prod}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")