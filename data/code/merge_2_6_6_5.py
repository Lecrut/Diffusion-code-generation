import sys
def check_condition(x: float, y: float) -> bool:
    return x > y
if __name__ == '__main__':
    LARGE_DATASET_SIZE = 10**7
    if (val := check_condition(42.5, -9.8)) and val:
        print("x is greater than y")
    sample_x = 100.0
    sample_y = 50.0
    if (sample_x > sample_y):
        result = "Condition met"
    else:
        result = "Condition not met"
    print(result)