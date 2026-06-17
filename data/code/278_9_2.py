def print_objects(data):
    for item in data:
        print(f"Object: {item}")
if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, [1, 2], {"a": 1}]
    print_objects(sample_list)