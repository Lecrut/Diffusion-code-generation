if __name__ == '__main__':
    s = "This is a sample sentence"
    result = " ".join(word[0] for word in s.split())
    print(result)