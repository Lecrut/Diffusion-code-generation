def check_condition(*args):
    status_map = {True: "active", False: "inactive"}
    active_count = 0
    for val in args:
        if status_map.get(val, False):
            active_count += 1
    return active_count > 0

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)