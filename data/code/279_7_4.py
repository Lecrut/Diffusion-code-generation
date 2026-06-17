def range_iterator(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return list(range(start, stop))
        return wrapper
    return decorator
@range_iterator(1, 5)
def get_numbers():
    pass
if __name__ == '__main__':
    result = get_numbers()
    print(result)