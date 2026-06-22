if __name__ == '__main__':
    s = 'Python'
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    
    for char in s:
        print(char)