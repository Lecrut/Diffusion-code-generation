def compare_lengths(len1, len2):
    result = "len1 is greater" if len1 > len2 else ("len2 is smaller" if len2 < len1 else "equal")
    return result

if __name__ == '__main__':
    lengths_to_compare = [
        (10, 10),
        (25, 15),
        (5, 20),
        (100, 50)
    ]
    
    for len1, len2 in lengths_to_compare:
        print(f"Comparing {len1} and {len2}: {compare_lengths(len1, len2)}")