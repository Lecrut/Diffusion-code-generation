def append_exclamation(string):
    return f"{string}!"

if __name__ == '__main__':
    greetings = ("Hello", "World", "Python")
    modified_greetings = tuple(append_exclamation(greet) for greet in greetings)
    print(modified_greetings)