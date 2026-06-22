def concatenate_and_greet(greeting, name):
    GREETING_DELIMITER = ", "
    EXCLAMATION_MARK = "!"
    return greeting + GREETING_DELIMITER + name + EXCLAMATION_MARK

if __name__ == '__main__':
    sample_greeting = "Hello"
    sample_name = "World"
    result = concatenate_and_greet(sample_greeting, sample_name)
    print(result)