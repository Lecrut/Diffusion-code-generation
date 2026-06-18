def combined_generator(str1: str, str2: str) -> None:
    for char in (str1 + str2):
        yield char
if __name__ == '__main__':
    result = list(combined_generator("Hello", "World"))
    print(result)