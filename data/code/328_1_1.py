if __name__ == '__main__':
    sample_string = "example"
    try:
        length = len(sample_string)
        print(length)
    except TypeError:
        print("Error: Input was not a string.")