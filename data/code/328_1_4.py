if __name__ == '__main__':
    sample_string = "Hello World"
    try:
        length = len(sample_string)
        print(length)
    except Exception as e:
        print("An error occurred")