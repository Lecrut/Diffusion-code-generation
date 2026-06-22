def compare_lengths(len1, len2):
    try:
        if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
            raise ValueError("Both lengths must be numbers.")
        
        result = "len1 is greater" if len1 > len2 else "len2 is smaller"
        return result if len1 != len2 else "equal"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    a = 10
    b = 5
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    
    a = 7.5
    b = 7.5
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")
    
    a = "ten"
    b = 10
    print(f"Comparing {a} and {b}: {compare_lengths(a, b)}")