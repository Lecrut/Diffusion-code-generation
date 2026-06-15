def print_mixed_list(data):
    for item in data:
        print(f"Item: {item}, Type: {type(item)}")
if __name__ == '__main__':
    sample_data = [10, "hello", 3.14, True, [1, 2], None]
    print_mixed_list(sample_data)