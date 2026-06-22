def find_shortest_string(strings):
    if not strings:
        raise ValueError("Input list cannot be empty")
    shortest = strings[0]
    for string in strings[1:]:
        if len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    try:
        print(find_shortest_string(sample_strings))
    except ValueError as e:
        print(e)