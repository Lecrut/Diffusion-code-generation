def product_pairs(A, B):
    for a in A:
        for b in B:
            yield a * b
if __name__ == '__main__':
    list_a = [1, 2, 3]
    list_b = [10, 20]
    result_generator = product_pairs(list_a, list_b)
    results = list(result_generator)
    print(results)