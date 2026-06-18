def check_greater():
    x = 10
    y = 5
    return "x is greater than y" if x > y else f"x ({x}) is not greater than y ({y})"

if __name__ == '__main__':
    print(check_greater())