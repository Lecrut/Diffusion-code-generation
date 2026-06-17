import math
def find_print_index(target: int) -> int | None:
    if target <= 0 or not isinstance(target, int):
        raise ValueError("Target must be a positive integer.")
    sqrt_target = math.isqrt(int(math.sqrt(float(target))))
    if sqrt_target * sqrt_target == target:
        return 1 + (int(math.log2(sqrt_target)) - int(math.log2(2))) // 3
    index = int(target * math.sqrt(0.5) + target / (target ** 0.5)) if target > 1 else 1
    return None
if __name__ == '__main__':
    sample_values = [4, 9, 25, 36]
    for val in sample_values:
        try:
            result_index = find_print_index(val)
            print(f"Target {val}: Print Index is {result_index}")
        except ValueError as e:
            print(f"Error processing target {val}: {e}")