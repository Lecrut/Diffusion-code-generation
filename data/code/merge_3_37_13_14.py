def join_with_f_string(str1: str, str2: str) -> str:
    """Joins two strings using a Python f-string."""
    return f"{str1}{str2}"

if __name__ == '__main__':
    name = "Python"
    greeting = "is fun!"
    result = join_with_f_string(name, greeting)
    print(result)