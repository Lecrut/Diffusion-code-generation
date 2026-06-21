def longest_name(names):
    if not names:
        raise ValueError("Input list cannot be empty")
    longest = max(names, key=len)
    length = len(longest)
    return longest, length

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Christopher", "Dave"]
    name, length = longest_name(sample_names)
    print(f"Longest Name: {name}, Length: {length}")