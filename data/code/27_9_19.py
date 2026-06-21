def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    triplets = [(3, 4, 5), (1, 2, 3), (5, 5, 5), (1, 1, 2), (10, 10, 10), (0, 0, 0)]
    results = [is_valid_triangle(a, b, c) for a, b, c in triplets]
    for res in results:
        print(res)