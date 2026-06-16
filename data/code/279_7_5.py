def range_iterator(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return list(range(start, stop))
        return wrapper
    return decorator
@range_iterator(1, 10)
def iterate_numbers():
    pass
if __name__ == '__main__':
    result = iterate_numbers()
    print(result)