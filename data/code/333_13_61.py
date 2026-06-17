import re
input_str = "Hello World Python Programming"
result = [word[0] for word in input_str.split() if len(word) > 0]
print("".join(result))
if __name__ == '__main__':
    pass