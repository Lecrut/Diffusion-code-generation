if __name__ == '__main__':
    items = {f"Item {i+1}": f"Category {i//3+1}" for i in range(9)}
    sample_items = [items[f"Item {i+1}"] for i in range(10)]
    print(sample_items)