import sys
def check_condition(x: int, y: int) -> bool:
    if (val := x > y):
        return val
    return False
if __name__ == '__main__':
    large_dataset = [10**9] * 1_000_000
    threshold = sum(large_dataset[:5]) // 2
    result = check_condition(threshold, 0)
    if result:
        print("Condition met")
    else:
        print("Condition not met")