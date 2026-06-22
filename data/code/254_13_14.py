MIN_STRING_LENGTH = 1

def find_shortest_string(strings):
    if not strings:
        return None
    shortest = strings[0]
    for string in strings[1:]:
        if len(string) < MIN_STRING_LENGTH or len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_shortest_string(sample_strings))