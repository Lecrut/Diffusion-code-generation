def zip_compare(list_a, list_b):
    return [
        (x, y, 'less' if x < y else 'greater' if x > y else 'equal')
        for x, y in zip(list_a, list_b)
    ]

if __name__ == '__main__':
    sample_a = [10, 20, 30]
    sample_b = [15, 10, 30]
    results = zip_compare(sample_a, sample_b)
    for val_a, val_b, relation in results:
        print(f"{val_a}, {val_b} -> {relation}")