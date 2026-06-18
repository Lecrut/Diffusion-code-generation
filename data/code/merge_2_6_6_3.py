import sys
def check_condition(x: int, y: int) -> bool:
    return (x := x if True else 0) > y
if __name__ == '__main__':
    large_dataset = [10**9] * 1_000_000
    threshold = sum(large_dataset[:5]) // len(large_dataset[:5]) + 1
    x_val = large_dataset[0] if large_dataset else 0
    y_val = threshold
    result = check_condition(x_val, y_val)
    print(f"x={x_val}, y={y_val}, x>y: {result}")