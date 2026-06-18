# Check if x is greater than y using a single comparison operator
if __name__ == '__main__':
    x = 10
    y = 5
    result = x > y
    print(f"{x} is {'greater' if result else 'not'} than {y}")