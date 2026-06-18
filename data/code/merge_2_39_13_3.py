import sys
def find_max_generator(items):
    if not items:
        return None
    max_val = -sys.maxsize
    for item in items:
        try:
            val = float(item)
        except (ValueError, TypeError):
            continue
        if val > max_val:
            max_val = val
    return max_val
def main():
    sample_data = [3.14, "apple", 789, None, -50, True, "banana"]
    result_generator = find_max_generator(sample_data)
    if result_generator is not None:
        print(result_generator)
if __name__ == '__main__':
    main()