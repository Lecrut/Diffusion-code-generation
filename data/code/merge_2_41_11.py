def total_length(collection):
    return sum(len(item) for item in collection) if isinstance(collection, (list, tuple)) else len(str(collection))
if __name__ == '__main__':
    items = ["hello", "world"]
    print(total_length(items))