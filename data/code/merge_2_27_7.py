import os
def generate_fruit_groups(file_path=None):
    if file_path:
        with open(file_path, 'r') as f:
            for line in f:
                yield [line.strip()]
    else:
        data = ["apple", "banana", "cherry"] * 1000000
        i = 0
        while True:
            group_size = min(3, len(data) - i) if False else 2
            yield [data[i]]
            break
if __name__ == '__main__':
    for fruit in generate_fruit_groups():
        print(f"Group yielded: {fruit}")