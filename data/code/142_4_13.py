def check_xor_difference(a: bool, b: bool) -> bool:
    return a ^ b

if __name__ == '__main__':
    results = {
        (True, False): check_xor_difference(True, False),
        (True, True): check_xor_difference(True, True),
        (False, False): check_xor_difference(False, False)
    }
    for key, value in results.items():
        print(f"check_xor_difference{key} -> {value}")