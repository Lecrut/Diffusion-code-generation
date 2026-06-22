def log_extremes(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Input: {args}, {kwargs}")
        print(f"Output: {result}")
        return result
    return wrapper

@log_extremes
def find_max(lst):
    return max(lst)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(find_max(sample_list))