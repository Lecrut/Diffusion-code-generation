def later_string(s1, s2):
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("Both arguments must be strings")
    return max(s1, s2)

if __name__ == '__main__':
    print(later_string("apple", "banana"))