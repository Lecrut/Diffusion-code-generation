def count_and_check_exclusive(b1: bool, b2: bool, b3: bool, b4: bool, b5: bool) -> bool:

    def count_true_bits(x):
        x -= x >> 1 & 1431655765
        x = (x & 858993459) + (x >> 2 & 858993459)
        return (x + (x >> 4) & 4042322160) % 256
    combined = int(b1) * 1 + int(b2) * 2 + int(b3) * 4 + int(b4) * 8 + int(b5) * 16
    true_count = count_true_bits(combined)
    return true_count == 1
if __name__ == '__main__':
    result = count_and_check_exclusive(True, False, True, False, False)
    print(result)