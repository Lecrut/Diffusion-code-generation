def find_longest_name(names):
    if not names:
        return None, 0
    longest = max(names, key=len)
    length = len(longest)
    return longest, length

if __name__ == '__main__':
    sample_names = ["Eve", "Frank", "Grace", "Hank"]
    name, length = find_longest_name(sample_names)
    print(f"Longest Name: {name}, Length: {length}")