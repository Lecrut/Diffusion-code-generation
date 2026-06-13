import sys
if __name__ == '__main__':
    names_input = "Alice\nBob\nCharlie\nAlice\nDavid\nBob"
    names = names_input.splitlines()
    unique_names = set(names)
    sorted_names = sorted(list(unique_names), reverse=True)
    for name in sorted_names:
        print(name)