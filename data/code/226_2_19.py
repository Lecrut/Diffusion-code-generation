if __name__ == '__main__':
    sample_string = 'Hello World'
    repetitions = 100
    result = '\n'.join([sample_string for _ in range(repetitions)])
    print(result)