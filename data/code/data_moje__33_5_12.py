import functools

@functools.lru_cache(maxsize=128)
def triangle_area(base, height):
    return base * height * 0.5

if __name__ == '__main__':
    result = triangle_area(10, 5)
    print(result)
    result = triangle_area(10, 5)
    print(result)
    result = triangle_area(7, 3)
    print(result)