def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    triplets = [(3, 4, 5), (1, 2, 3), (10, 2, 5), (7, 7, 7), (0, 5, 5), (1.5, 2.5, 3.0)]
    results = [is_valid_triangle(*triplet) for triplet in triplets]
    for result in results:
        print(result)