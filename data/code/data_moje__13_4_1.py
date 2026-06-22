from itertools import islice

def get_nth(gen, n):
    try:
        return next(islice(gen, n, None))
    except StopIteration:
        return None

if __name__ == '__main__':
    result = get_nth((x for x in range(10)), 5)
    print(result)