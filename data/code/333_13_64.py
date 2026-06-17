s = "hello world python"
result = [word[0] for word in s.split() if len(word) > 0]
print("".join(result))
if __name__ == '__main__':
    pass