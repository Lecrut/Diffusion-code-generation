def repeat_string():
    target_string = "Hello World"
    count = 100
    result = ""
    for _ in range(count):
        result += target_string + "\n"
    print(result.rstrip())
if __name__ == '__main__':
    repeat_string()