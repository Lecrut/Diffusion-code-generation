import sys
def generate_fruits():
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    while True:
        for fruit in fruits:
            yield fruit
if __name__ == '__main__':
    group_size = 3
    try:
        with open("fruits_data.txt", "w") as f_out, sys.stdin as input_stream:
            if not hasattr(input_stream, 'read'):
                print(f"Generating {group_size} fruit groups per cycle...")
                gen = generate_fruits()
                while True:
                    group = []
                    try:
                        for _ in range(group_size):
                            item = next(gen)
                            group.append(item)
                    except StopIteration:
                        break
                    print(f"Group {len(group)}:", ", ".join(group))
    except FileNotFoundError:
        gen = generate_fruits()
        while True:
            group = []
            try:
                for _ in range(group_size):
                    item = next(gen)
                    group.append(item)
            except StopIteration:
                break
            print(f"Group {len(group)}:", ", ".join(group))