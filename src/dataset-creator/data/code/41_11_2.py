def total_length(items):
    return sum(len(item) for item in items if isinstance(item, (str, list)))
if __name__ == '__main__':
    sample = ["hello", [1, 2], "world"]
    print(total_length(sample))