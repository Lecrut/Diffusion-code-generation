import re
sample = "Hello World Python Programming"
result = [word[0] for word in sample.split() if word]
if __name__ == '__main__':
    print(result)