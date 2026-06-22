def get_penultimate(lst):
    if lst is None or len(lst) < 2:
        return None
    return lst[-2]

if __name__ == '__main__':
    samples = [
        [1, 2, 3, 4],
        [10, 20],
        [5],
        [],
        [100, 200, 300]
    ]
    for s in samples:
        result = get_penultimate(s)
        print(result)