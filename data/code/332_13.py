if __name__ == '__main__':
    s = "Hello World"
    result = sum(1 for char in s if char.lower() in 'aeiou')
    print(result)