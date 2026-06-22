import functools

@functools.lru_cache(maxsize=None)
def triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    result = triangle_area(10, 5)
    print(result)