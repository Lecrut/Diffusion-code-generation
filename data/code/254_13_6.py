SHORT_STRINGS = ["apple", "banana", "cherry", "date"]

def find_shortest_string(strings):
    if not strings:
        return None
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == '__main__':
    print(find_shortest_string(SHORT_STRINGS))