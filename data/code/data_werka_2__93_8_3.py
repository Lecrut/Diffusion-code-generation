def check_both_false(val_a: bool, val_b: bool) -> bool:
    status_map = {
        (True, True): "both true",
        (True, False): "a true",
        (False, True): "b true",
        (False, False): "both false"
    }
    return status_map.get((val_a, val_b), None) == "both false"

if __name__ == '__main__':
    result = check_both_false(False, False)
    print(result)