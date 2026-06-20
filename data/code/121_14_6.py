def later_string(s1, s2):
    return s2 if s1 < s2 else s1

if __name__ == '__main__':
    print(later_string("apple", "banana"))