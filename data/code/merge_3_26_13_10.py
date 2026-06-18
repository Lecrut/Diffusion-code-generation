def check_first_greater_than_second(lst):
    return lambda lst: all(isinstance(x, (int, float)) and x > 0 for x in [lst[0], lst[1]]) if len(lst) >= 2 else None or False

if __name__ == '__main__':
    data = [5, 3]
    result = check_first_greater_than_second(data)(data)
    print(result)