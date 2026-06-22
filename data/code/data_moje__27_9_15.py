def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

if __name__ == '__main__':
    triplets = [(3, 4, 5), (1, 2, 3), (5, 12, 13), (2, 2, 4), (10, 15, 20)]
    results = [is_valid_triangle(*t) for t in triplets]
    for r in results:
        print(r)