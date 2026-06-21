def is_valid_triangle(sides):
    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)

if __name__ == '__main__':
    triplets = [
        [3, 4, 5],
        [1, 2, 3],
        [10, 10, 10],
        [0, 0, 0],
        [1, 1, 2]
    ]
    results = [is_valid_triangle(t) for t in triplets]
    for res in results:
        print(res)