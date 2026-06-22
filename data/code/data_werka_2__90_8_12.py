def check_condition(*args):
    status_map = {
        True: "active",
        False: "inactive"
    }
    active_count = 0
    for val in args:
        label = status_map.get(val)
        if label == "active":
            return True
    return False

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)