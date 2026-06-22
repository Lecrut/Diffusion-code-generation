def find_shortest_string(strings):
    if not strings:
        return None
    shortest = min(strings, key=len)
    return shortest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_shortest_string(sample_strings))