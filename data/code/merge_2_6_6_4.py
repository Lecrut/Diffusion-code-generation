import sys
def check_condition(x: int, y: int) -> bool:
    return (x > y) and not ((x - 10**9) % 2 == 0 if x else False)
if __name__ == '__main__':
    large_dataset = [i for i in range(1_000_000)]
    x, y = large_dataset[5], large_dataset[-5]
    result = check_condition(x, y)
    print(f"x={x}, y={y}, condition_met={result}")