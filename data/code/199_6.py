import sys
if __name__ == '__main__':
    input_data = "Alice\nBob\nCharlie\nAlice\nDavid\nBob"
    names = input_data.splitlines()
    unique_names = set(names)
    sorted_names = sorted(list(unique_names), reverse=True)
    for name in sorted_names:
        print(name)