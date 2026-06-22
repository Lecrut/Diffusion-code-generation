def find_shortest_string(strings):
    if not strings:
        raise ValueError("The list of strings cannot be empty")
    
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest

if __name__ == '__main__':
    sample_strings = ["apple", "banana", "cherry", "date"]
    print(find_shortest_string(sample_strings))