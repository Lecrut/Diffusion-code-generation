def compare_booleans(flag1: bool, flag2: bool) -> bool:
    return flag1 == flag2

if __name__ == '__main__':
    results = {
        (True, True): compare_booleans(True, True),
        (False, False): compare_booleans(False, False),
        (True, False): compare_booleans(True, False),
        (False, True): compare_booleans(False, True)
    }
    for key, value in results.items():
        print(f"compare_booleans{key} = {value}")