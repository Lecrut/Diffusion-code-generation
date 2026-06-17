def total_length(collection):
    return sum(len(item) for item in collection if isinstance(item, (str, list)))
if __name__ == '__main__':
    sample = ["hello", [1, 2], "world"]
    print(total_length(sample))