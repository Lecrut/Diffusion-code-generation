def find_longest_name(names):
    if not names:
        return None, 0
    
    longest_name = max(names, key=len)
    name_length = len(longest_name)
    
    return longest_name, name_length

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    name, length = find_longest_name(sample_names)
    print(f"Longest name: {name}, Length: {length}")